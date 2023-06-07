# Importing the API and instantiating the REST client according to our keys

#Importing the API and instantiating the REST client according to our keys
from alpaca.trading.client import TradingClient

API_KEY = "PK756R9JT97GESCBUZIV"
SECRET_KEY = "xfpnK4bk8oyzkOzxMqrEBcDavIFwZ1W8iYdMdCki"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

#Getting account information and printing it
# account = trading_client.get_account()
# for property_name, value in account:
#   print(f""{property_name}": {value}")
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

#Setting parameters for our buy orde
market_order_data = MarketOrderRequest(
    symbol="TXG",
    qty=5,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.GTC
  )

#Submitting the order and then printing the returned object
#market_order = trading_client.submit_order(market_order_data)
#for property_name, value in market_order:
#print(f""{property_name}": {value}")
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

#keys required for stock historical data client
client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

#multi symbol request - single symbol is similar
multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["TXG"])

latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_quotes["TXG"].ask_price

from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from datetime import datetime, timedelta
request_params = StockBarsRequest(
                        symbol_or_symbols=["TXG"],
                        timeframe=TimeFrame.Day,
                        start=datetime.now() - timedelta(days = 7),
                        end=datetime.now()
                        )
data = client.get_stock_bars(request_params)
print(data)
