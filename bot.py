from coinbase.wallet.client import Client

API_KEY = ''
API_SECRET = ''

# Currency pairs
BTC_USD = 'BTC-USD'

class CoinbaseBot:

    def __init__(self, api_key, api_secret):
        """
        Initializes an instance of the CoinbaseBot class. Initializes and sets the Coinbase API client.

        Args:
            api_key:str: API key for authenticating with the Coinbase API.
            api_secret:str: API secret for authenticating with the Coinbase API.
            client:coinbase.wallet.client.Client: Client object for authenticating using the provided api_key and api_secret. 
        """

        self.api_key = api_key
        self.api_secret = api_secret

        self.client = Client(self.api_key, self.api_secret)


    def live_prices(self, buy_currency_pair=None, sell_currency_pair=None):
        """
        Fetches the current buy price and sell price for specified cryto currency pairs. Can be same currency pair, or individual.

        Args:
            buy_currency_pair:str: The currency pair for which to get the current buy price. Formatted like so "XXX-XXX". See Coinbase documentation.
            sell_currency_pair:str: The currency pair for which to get the current buy price. Formatted like so "XXX-XXX". See Coinbase documentation.
        
        Returns:
            dict: Most recent buy and sell data for the specified currency pair. 
                  Includes the "amount" or price, and two individual fields denoting the pair.
        """

        combined_data = {}

        buy_data = self.live_buy_price(buy_currency_pair)
        sell_data = self.live_sell_price(sell_currency_pair)

        combined_data['buy'] = buy_data
        combined_data['sell'] = sell_data

        return combined_data


    def live_buy_price(self, currency_pair):
        """
        Fetches the current buy price for a given cryto currency pair.

        Args:
            currency_pair:str: The currency pair for which to get the current buy price. Formatted like so "XXX-XXX". See Coinbase documentation.

        Returns:
            dict: Key value dictionary object.
        """

        return self.client.get_buy_price(currency_pair=currency_pair)


    def live_sell_price(self, currency_pair):
        """
        Fetches the current sell price for a given cryto currency pair.

        Args:
            currency_pair:str: The currency pair for which to get the current buy price. Formatted like so "XXX-XXX". See Coinbase documentation.
        
        Returns:
            dict: Key value dictionary object.
        """

        return self.client.get_sell_price(currency_pair=currency_pair)




if __name__ == '__main__':
    bot = CoinbaseBot(API_KEY, API_SECRET)
    market_data = bot.live_prices(buy_currency_pair=BTC_USD, sell_currency_pair=BTC_USD)

    print(market_data)



# user = client.get_current_user()
# accounts = client.get_accounts()