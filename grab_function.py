import requests
import json
import boto3

def main(ticker):
    print(f"Making a request to API for {ticker} and adding to database...")
    # Pulls the data from the API
    response = pullData(ticker)
    
    # Adds the data to the dynamoDB
    addToDynamoDB(response.json())
    
    return(response.status_code)
    
def pullData(ticker):
    url = 'https://www.alphavantage.co/query?'
    token = 'Z0XJ5BZAJ049UV97'
    function = "TIME_SERIES_WEEKLY"
    
    params = {
      'symbol': ticker,
      'apikey': token,
      'function': function,
      'datatype': 'json'
    }
    
    response = requests.request('GET', url, params=params)
    return(response)
    
def addToDynamoDB(resp):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('WeeklyStock')
    
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