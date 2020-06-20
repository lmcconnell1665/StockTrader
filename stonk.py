import click
import grab_function
import clear_function

CONTEXT_SETTINGS = dict(help_option_names=['--help'])

# Name of the DynamoDB table that will hold the data
DYNAMO_DB_TABLE_NAME = 'WeeklyStock'

# AWS Region where the DynamoDB table is located
AWS_REGION = 'us-east-1'

# URL of the API that is providing stock data (AlphaVantage used when built)
URL = 'https://www.alphavantage.co/query?'

# API Token used to authenticate with the API (You can get one for free at https://www.alphavantage.co)
TOKEN = 'Z0XJ5BZAJ049UV97'

# The data set that should be targeted (options are in AlphaVantage documentation)
TIMEFRAME = 'TIME_SERIES_WEEKLY'

@click.group(context_settings=CONTEXT_SETTINGS) 
def main():
    """
    Luke McConnell's stock trading command line tool for adding and removing data from AWS DynamoDB using boto3
    
    \b
    Created: 06/15/2020
    Updated: 06/20/2020
    """
    return

# GRAB COMMAND
@main.command()
@click.option(
    "--api_token",
    prompt="Token to authenticate with API",
    help="Pass in the token to authenticate with the API.",
    default=TOKEN)

@click.option(
    "--ticker",
    prompt="Ticker of stock to grab",
    help="Pass in the ticker of the stock to grab (i.e AAPL).")
    
def grab(ticker, api_token):
    """
    Pull in stock data from API
    """
    # print(grab_function.main(f"{ticker}"))
    grab_function.main(f"{ticker}", DYNAMO_DB_TABLE_NAME, AWS_REGION, URL, f"{api_token}", TIMEFRAME)
    print("DONE grabbing")
    
# CLEAR COMMAND
@main.command()
@click.option(
    "--ticker",
    prompt="Ticker of stock to delete",
    help="Pass in the ticker of the stock to delete (i.e AAPL).")
    
def clear(ticker):
    """
    Clear all stock data from the database
    """
    clear_function.main(f"{ticker}", DYNAMO_DB_TABLE_NAME, AWS_REGION)
    print("DONE deleting")

if __name__ == '__main__':
    main()