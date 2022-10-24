import os
import time
import chromedriver_autoinstaller

from colorama import Fore
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pkg import c_print


class Phantom:
    def __init__(self, service_config: dict, user_config: dict):
        self.service_config = service_config
        self.user_config = user_config

        self.__path_to_extension = "../serviceConfig/Phantom.crx"

    @staticmethod
    def __select_element(xpath: str, to_be_clicked: bool, driver: webdriver.Chrome, input_key: str = "") -> None:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
        el = driver.find_element(By.XPATH, xpath)

        if input_key != "":
            el.send_keys(input_key)
            to_be_clicked = False

        if to_be_clicked:
            el.click()

    @staticmethod
    def __is_element_exists(driver: webdriver.Chrome, xpath: str) -> bool:
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def setup_driver(self) -> webdriver.Chrome:
        chromedriver_autoinstaller.install()

        options = Options()

        options.add_extension(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.__path_to_extension))
        options.add_argument("--disable-gpu")

        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        os.environ['WDM8LOCAL'] = '1'

        driver = webdriver.Chrome(options=options)

        return driver

    def init_wallet(self, driver: webdriver.Chrome) -> None:
        c_print("Init wallet...", Fore.YELLOW)

        driver.switch_to.window(driver.window_handles[1])

        self.__select_element(self.service_config.get("elements").get("phantom").get("importButton"), True, driver)

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='word_0']")))
        for i in range(0, 12):
            driver.find_element(By.XPATH, f"//*[@id='word_{i}']").send_keys(self.user_config.get("seed").split(' ')[i])

        self.__select_element(self.service_config.get("elements").get("phantom").get("submitButton"), True, driver)

        self.__select_element(self.service_config.get("elements").get("phantom").get("selectWallet"), True, driver)

        time.sleep(5)
        self.__select_element(self.service_config.get("elements").get("phantom").get("submitButton"), True, driver)

        self.__select_element(self.service_config.get("elements").get("phantom").get("passwordField"), False, driver,
                              input_key=self.user_config.get("password"))
        self.__select_element(self.service_config.get("elements").get("phantom").get("confirmPasswordField"), False,
                              driver,
                              input_key=self.user_config.get("password"))

        self.__select_element(self.service_config.get("elements").get("phantom").get("checkbox"), True, driver)
        self.__select_element(self.service_config.get("elements").get("phantom").get("submitButton"), True, driver)

        time.sleep(5)
        self.__select_element(self.service_config.get("elements").get("phantom").get("continueButton"), True, driver)

        time.sleep(5)
        self.__select_element(self.service_config.get("elements").get("phantom").get("continueButton"), True, driver)

        driver.switch_to.window(driver.window_handles[0])

        c_print("Done\n", Fore.YELLOW)

    def select_wallet(self, driver: webdriver.Chrome) -> None:
        c_print("Selecting wallet...", Fore.YELLOW)

        self.__select_element(self.service_config.get("elements").get("magiceden").get("connectWallet"), True, driver)

        time.sleep(2)
        self.__select_element(self.service_config.get("elements").get("magiceden").get("phantomWallet"), True, driver)
        time.sleep(2)

        if len(driver.window_handles) >= 2:
            WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])

            time.sleep(2)
            self.__select_element(self.service_config.get("elements").get("magiceden").get("popup").get("connectButton"), True, driver)

            driver.switch_to.window(driver.window_handles[0])
            c_print("Done\n", Fore.YELLOW)

    def make_purchase(self, driver: webdriver.Chrome, url: str) -> None:
        try:
            c_print("Making purchase...", Fore.YELLOW)

            driver.get(url)

            if self.__is_element_exists(driver, self.service_config.get("elements").get("magiceden").get("connectWallet")):
                self.select_wallet(driver)

            self.__select_element(self.service_config.get("elements").get("magiceden").get("buyButton"), True, driver)

            WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])

            self.__select_element(self.service_config.get("elements").get("magiceden").get("popup").get("approveButton"), True, driver)

            WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(1))
            time.sleep(5)

            c_print(f"Success! Your purchase - {url}", Fore.GREEN)
        except Exception as err:
            c_print(f"An error has occurred: {err}", Fore.RED)
        finally:
            if self.user_config.get("close_browser"):
                c_print("Stop working...", Fore.RED)
                driver.quit()

            exit()
