import requests
import boto3

def main(ticker, table_name, aws_region, api_url, api_token, time_frame):
    print(f"Making a request to API for {ticker} and adding to database...")
    # Pulls the data from the API
    response = pullData(ticker, api_url, api_token, time_frame)
    
    # Adds the data to the dynamoDB
    addToDynamoDB(response.json(), table_name, aws_region)
    
    return(response.status_code)
    
def pullData(ticker, api_url, api_token, time_frame):
    url = api_url
    token = api_token
    function = time_frame
    
    params = {
      'symbol': ticker,
      'apikey': token,
      'function': function,
      'datatype': 'json'
    }
    
    response = requests.request('GET', url, params=params)
    return(response)
    
def addToDynamoDB(resp, table_name, aws_region):
    dynamodb = boto3.resource('dynamodb', region_name=aws_region)
    table = dynamodb.Table(table_name)
    
    with table.batch_writer() as batch:

        for row in resp['Weekly Time Series']:
            item = {
                'ticker': resp['Meta Data']['2. Symbol'],
                'date': row,
                'open': resp['Weekly Time Series'][row]['1. open'],
                'high': resp['Weekly Time Series'][row]['2. high'],
                'low': resp['Weekly Time Series'][row]['3. low'],
                'close': resp['Weekly Time Series'][row]['4. close'],
                'volume': resp['Weekly Time Series'][row]['5. volume']
            }
            
            batch.put_item(item)

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()