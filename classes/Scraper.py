import requests
from colorama import Fore

from config import COLLECTION_URL, WILLING_PRICE
from helpers.utils import cPrint


class Scraper:
    def __init__(self):
        self.baseUrl = 'https://api-mainnet.magiceden.dev/v2/'

    def getListings(self):
        symbol = COLLECTION_URL.split("/")[-1]
        cPrint(f'Getting all listed NFTs from collection [{symbol}]...', Fore.YELLOW)

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

    def getEligibleListings(self, listings):
        eligibleListings = list()
        listingPrices = list()

        for listing in listings:
            if listing['price'] <= WILLING_PRICE:
                eligibleListings.append(listing)
                listingPrices.append(listing['price'])

        return eligibleListings, listingPrices
