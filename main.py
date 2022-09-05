import time

from colorama import Fore

from classes import PhantomBot
from classes import Scraper
from helpers.utils import cPrint, isListingsOk

from config import COOLDOWN

BOT = PhantomBot()
SCRAPER = Scraper()

if __name__ == "__main__":
    driver = BOT.setupDriver()

    driver.get("https://www.magiceden.io/")
    driver.maximize_window()

    BOT.initWallet(driver)
    BOT.selectWallet(driver)

    while True:
        listings = SCRAPER.getListings()
        eligibleListings, listingPrices = SCRAPER.getEligibleListings(listings)

        if isListingsOk(eligibleListings, listingPrices):
            lowestPrice = min(listingPrices)
            bestOffer = str()

            for listing in eligibleListings:
                if float(listing['price']) == float(lowestPrice):
                    bestOffer = f'https://www.magiceden.io/item-details/{listing["tokenMint"]}'

            if len(bestOffer) > 0:
                cPrint(f'Found the best offer - {bestOffer}', Fore.GREEN)
                try:
                    pass
                    BOT.makePurchase(driver, bestOffer)
                except Exception as err:
                    cPrint(f'Unable to purchase: {err}', Fore.RED)
                finally:
                    break
            else:
                cPrint("Couldn't find a suitable offer", Fore.YELLOW)
                cPrint(f"Next try in {COOLDOWN / 60} minutes", Fore.YELLOW)

                time.sleep(COOLDOWN)
