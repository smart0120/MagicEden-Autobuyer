import time

from colorama import Fore
from selenium.webdriver.chrome.webdriver import WebDriver

from config import user_config
from internal.magiceden import MagicEden
from internal.phantom import Phantom
from pkg import init_yaml, c_print


def start_buying(magiceden: MagicEden, phantom: Phantom, driver: WebDriver) -> None:
    while True:
        listings = magiceden.get_listings()
        eligible_listings, listing_prices = magiceden.get_eligible_listings(listings)

        if magiceden.is_listings_ok(eligible_listings, listing_prices):
            lowest_price = min(listing_prices)
            best_offer = str()

            for listing in eligible_listings:
                if float(listing['price']) == float(lowest_price):
                    best_offer = f'https://www.magiceden.io/item-details/{listing.get("tokenMint")}'

            if len(best_offer) > 0:
                c_print(f'Found the best offer - {best_offer}', Fore.GREEN)
                try:
                    phantom.make_purchase(driver, best_offer)
                except Exception as err:
                    c_print(f'Unable to purchase: {err}', Fore.RED)
                finally:
                    break
            else:
                c_print("Couldn't find a suitable offer", Fore.YELLOW)
                c_print(f"Next try in {user_config.get('cooldown') / 60} minutes", Fore.YELLOW)

                time.sleep(user_config.get("cooldown"))
        else:
            c_print("Couldn't find a suitable offer", Fore.YELLOW)
            c_print(f"Next try in {user_config.get('cooldown') / 60} minutes", Fore.YELLOW)

            time.sleep(user_config.get("cooldown"))


def main():
    service_config = init_yaml()

    phantom = Phantom(service_config, user_config)

    driver = phantom.setup_driver()

    phantom.init_wallet(driver)

    driver.get(user_config.get("collection_url"))

    phantom.select_wallet(driver)

    magiceden = MagicEden(user_config)

    start_buying(magiceden, phantom, driver)


if __name__ == "__main__":
    main()
