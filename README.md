![Python application test with Github Actions](https://github.com/lmcconnell1665/StockTrader/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# StockTrader
Command line tool for collecting stock information from the [AlphaVantage API](https://www.alphavantage.co) and storing the data in an AWS DynamoDB table.

## To install this command line tool
Clone this GitHub repo by running `git clone https://github.com/lmcconnell1665/StockTrader.git` from your terminal. 
Once the repository has been cloned, change into the repository directory by running `cd StockTrader`.

## To configure the tool
Open the `stonk.py` file and change the values for `DYNAMO_DB_TABLE_NAME` and `AWS_REGION` to match your environment.
You will need to create a DynamoDB table with `ticker` as the Primary partition key and `date` as the primary sort key.
Make sure that the name of that table matches your setting of `DYNAMO_DB_TABLE_NAME` in `stonk.py`.
The environment that you install the command line tool in will also need the proper AWS credentials to read and write to this DynamoDB table.

## To use this tool
There are two primary commands with this tool, grab and clear.
- grab: pull in stock data from API
- clear: clear all stock data from the database

Each command requires one argument (--ticker), which is the ticker that corresponds to the stock that you want to grab or clear.

### Grab command
Run `python stonk.py grab` from a terminal with your directory in `/StockTrader`.
You will be asked to enter an `api_key` to authenticate with the API.
You can set a default for this key by changing the value for `TOKEN` in `stonk.py`.
Once a default is set it will be displayed in brackets.
Just press `enter` to use the saved default value for the token.
You will be asked to enter a `ticker` for the stock you want to grab.
Once you see `DONE grabbing` the stocks historical information has been saved to the DynamoDB table.

### Clear command
Run `python stonk.py clear` from a terminal with your directory in `/StockTrader`.
You will be asked to enter a `ticker` for the stock you want to clear.
Once you see `DONE deleting` the stocks historical information has been removed from the DynamoDB table.

## Demo: Storing Stock API Data in DynamoDB
[![Demo: Storing Stock API Data in DynamoDB](http://img.youtube.com/vi/tU_yvEbdsPE/0.jpg)](http://www.youtube.com/watch?v=tU_yvEbdsPE "Demo: Storing Stock API Data in DynamoDB")
