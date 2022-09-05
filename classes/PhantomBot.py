import os
import time

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from helpers.utils import cPrint

from config import SEED_PHRASE, PASSWORD, CLOSE_BROWSER, ELEMENTS
from helpers.utils.utils import is_element_exists


class PhantomBot:
    def __init__(self):
        self.elements = ELEMENTS

    @staticmethod
    def setupDriver() -> webdriver.Chrome:
        options = Options()

        options.add_extension("Phantom.crx")
        options.add_argument("--disable-gpu")

        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        os.environ['WDM8LOCAL'] = '1'

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        return driver

    @staticmethod
    def __selectElement(xpath: str, toBeClicked: bool, driver: webdriver.Chrome, input_key: str = "") -> None:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
        el = driver.find_element(By.XPATH, xpath)

        if input_key != "":
            el.send_keys(input_key)
            toBeClicked = False

        if toBeClicked:
            el.click()

    def initWallet(self, driver: webdriver.Chrome) -> None:
        cPrint("Init wallet...", Fore.YELLOW)

        driver.switch_to.window(driver.window_handles[1])

        self.__selectElement(self.elements['phantom']['importButton'], True, driver)

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='word_0']")))
        for i in range(0, 12):
            driver.find_element(By.XPATH, f"//*[@id='word_{i}']").send_keys(SEED_PHRASE.split(' ')[i])

        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        self.__selectElement(self.elements['phantom']['passwordField'], False, driver,
                             input_key=PASSWORD)
        self.__selectElement(self.elements['phantom']['confirmPasswordField'], False, driver,
                             input_key=PASSWORD)
        self.__selectElement(self.elements['phantom']['checkbox'], True, driver)
        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['continueButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['continueButton'], True, driver)

        driver.switch_to.window(driver.window_handles[0])

        cPrint("Done\n", Fore.YELLOW)

    def selectWallet(self, driver: webdriver.Chrome) -> None:
        cPrint("Selecting wallet...", Fore.YELLOW)

        self.__selectElement(self.elements['magiceden']['connectWallet'], True, driver)

        time.sleep(2)
        self.__selectElement(self.elements['magiceden']['phantomWallet'], True, driver)

        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        time.sleep(2)
        self.__selectElement(self.elements['magiceden']['popup']['connectButton'], True, driver)

        driver.switch_to.window(driver.window_handles[0])
        cPrint("Done\n", Fore.YELLOW)

    def makePurchase(self, driver: webdriver.Chrome, url: str) -> None:
        try:
            cPrint("Making purchase...", Fore.YELLOW)

            driver.get(url)

            if is_element_exists(driver, self.elements['magiceden']['connectWallet']):
                self.selectWallet(driver)

            self.__selectElement(self.elements['magiceden']['buyButton'], True, driver)

            WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])

            self.__selectElement(self.elements['magiceden']['popup']['approveButton'], True, driver)

            WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(1))
            time.sleep(5)

            cPrint(f"Success!\nYour purchase - {url}", Fore.GREEN)
        except Exception as err:
            cPrint(f"An error has occurred: {err}", Fore.RED)
        finally:
            if CLOSE_BROWSER:
                cPrint("Stop working...", Fore.RED)
                driver.quit()

            exit()
