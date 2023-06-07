# Importing the API and instantiating the REST client according to our keys

from alpaca.trading.client import TradingClient

API_KEY = "PKQI33ZN8PL4OFTAVDWM"
SECRET_KEY = "jNa04HNvurPVwFKWGN0f0k9U7bZqfrCbIkkD5ODe"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Getting account information and printing it
# account = trading_client.get_account()
# for property_name, value in account:
#   print(f"\"{property_name}\": {value}")

from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Setting parameters for our buy order
market_order_data = MarketOrderRequest(
    symbol="TXG",
    qty=5,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.GTC
  )

# Submitting the order and then printing the returned object
market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
    print(f"\"{property_name}\": {value}")




from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

# keys required for stock historical data client
client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

# multi symbol request - single symbol is similar
multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price

print(latest_multisymbol_quotes.df)