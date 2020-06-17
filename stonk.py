import click
import grab_function
import clear_function

CONTEXT_SETTINGS = dict(help_option_names=['--help'])

@click.group(context_settings=CONTEXT_SETTINGS) 
def main():
    """
    Luke McConnell's stock trading command line tool
    
    \b
    Created: 06/15/2020
    Updated: 06/15/2020
    """
    return

# GRAB COMMAND
@main.command()
@click.option(
    "--ticker",
    prompt="Ticker of stock to grab",
    help="Pass in the ticker of the stock to grab (i.e AAPL).")
    
def grab(ticker):
    """
    Pull in stock data from API
    """
    # print(grab_function.main(f"{ticker}"))
    grab_function.main(f"{ticker}")
    print("DONE grabbing")
    
# CLEAR COMMAND
@main.command()
@click.option(
    "--ticker",
    prompt="Ticker of stock to delete",
    help="Pass in the ticker of the stock to delete (i.e AAPL).")
    
def clear(ticker):
    """
    Clear stock data from the database
    """
    clear_function.main(f"{ticker}")
    print("DONE deleting")

if __name__ == '__main__':
    main()