import requests
from colorama import Fore

from pkg import c_print


class MagicEden:
    def __init__(self, user_config: dict):
        self.baseUrl = 'https://api-mainnet.magiceden.dev/v2/'
        self.user_config = user_config

    @staticmethod
    def is_listings_ok(listings_: list, prices_: list) -> bool:
        return (len(listings_) == len(prices_)) and len(listings_) > 0 and len(prices_) > 0

    def get_listings(self) -> list:
        symbol = self.user_config.get("collection_url").split("/")[-1]
        c_print(f'Getting all listed NFTs from collection [{symbol}]...', Fore.YELLOW)

        listings = list()
        counter = 0

        while True:
            response = requests.get(self.baseUrl + f'collections/{symbol}/listings?offset={counter}').json()
            if len(response) < 1:
                break

            for i in range(len(response)):
                listings.append({'price': response[i]['price'], 'tokenMint': response[i]['tokenMint']})

            counter += len(response)

        return listings

    def get_eligible_listings(self, listings) -> (list, list):
        eligible_listings = list()
        listing_prices = list()

        for listing in listings:
            if listing['price'] <= self.user_config.get("willing_price"):
                eligible_listings.append(listing)
                listing_prices.append(listing['price'])

        return eligible_listings, listing_prices
