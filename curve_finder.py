import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd
import numpy as np

def query_and_store_data(selected_ticker, date_range, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('WeeklyStock')

    response = table.query(
        ProjectionExpression="ticker, #dt, #op, #cl, low, high",
        ExpressionAttributeNames={"#dt": "date", "#op": "open", "#cl": "close"},
        KeyConditionExpression=
            Key('ticker').eq(selected_ticker) & Key('date').between(date_range[0], date_range[1])
    )
    return response['Items']

def build_dataframe():
    query_ticker = 'CAT'
    query_range = ('2019-08-23', '2020-06-16')

    response = query_and_store_data(query_ticker, query_range)

    stockData = pd.DataFrame(columns = ['ticker','date','open','close','high','low'])

    for i in response:
        stockData = stockData.append(i, ignore_index=True)

    return(stockData)

def main():
    stock = build_dataframe()

    stock['open'] = pd.to_numeric(stock['open'])
    stock['close'] = pd.to_numeric(stock['close'])
    stock['open'] = pd.to_numeric(stock['high'])
    stock['open'] = pd.to_numeric(stock['low'])

    # return(stock)

if __name__ == '__main__':
    main()
    
    
