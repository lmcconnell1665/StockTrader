import boto3
from boto3.dynamodb.conditions import Key

def scan_database(selected_ticker, delete_records, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('WeeklyStock')
    
    scan_kwargs = {
        # Returns only items that satisfy the condition. All other items are discarded.
        'FilterExpression': Key('ticker').eq(selected_ticker),
        # Attributes that you want in the scan results
        'ProjectionExpression': "ticker, #dt",
        # Helps resolve problems with reserved words like year and date
        'ExpressionAttributeNames': {"#dt": "date"}

    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        
        delete_records(response.get('Items', []))
        
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
        
def delete_scan_results(resp, dynamodb=None):
    
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('WeeklyStock')
    
    with table.batch_writer() as batch:
        for record in resp:
            item = {
                'ticker': record['ticker'],
                'date': record['date']
            }
            
            batch.delete_item(item)
        
def main(passed_in_ticker):
    ticker = passed_in_ticker
    print(f"Scanning for stocks with the ticker {ticker} and deleting from database...")
    scan_database(ticker, delete_scan_results)

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()