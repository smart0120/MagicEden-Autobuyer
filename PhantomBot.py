import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


class PhantomBot:
    def __init__(self, config, elements):
        self.config = config
        self.elements = elements

    @staticmethod
    def setupDriver():
        options = Options()

        options.add_extension("Phantom.crx")
        options.add_argument("--disable-gpu")

        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        os.environ['WDM8LOCAL'] = '1'

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        return driver

    def initWallet(self, driver):
        print("Init wallet...")
        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.elements['phantom']['importButton'])))
        driver.find_element(By.XPATH, self.elements['phantom']['importButton']).click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='word_0']")))
        for i in range(0, 12):
            driver.find_element(By.XPATH, f"//*[@id='word_{i}']").send_keys(self.config["seedPhrase"].split(' ')[i])
        driver.find_element(By.XPATH, self.elements['phantom']['submitButton']).click()

        time.sleep(5)
        driver.find_element(By.XPATH, self.elements['phantom']['submitButton']).click()

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.elements['phantom']['passwordField'])))
        driver.find_element(By.XPATH, self.elements['phantom']['passwordField']).send_keys(self.config["password"])
        driver.find_element(By.XPATH, self.elements['phantom']['confirmPasswordField']).send_keys(self.config["password"])
        driver.find_element(By.XPATH, self.elements['phantom']['checkbox']).click()
        driver.find_element(By.XPATH, self.elements['phantom']['submitButton']).click()

        time.sleep(5)
        driver.find_element(By.XPATH, self.elements['phantom']['continueButton']).click()

        time.sleep(5)
        driver.find_element(By.XPATH, self.elements['phantom']['continueButton']).click()

        driver.switch_to.window(driver.window_handles[0])
        print('Done\n')

    def selectWallet(self, driver):
        print("Selecting wallet...")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, self.elements['magiceden']['connectWallet'])))
        main_wallet = driver.find_element(By.XPATH, self.elements['magiceden']['connectWallet'])
        main_wallet.click()

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.elements['magiceden']['phantomWallet'])))
        phantomExtension = driver.find_element(By.XPATH, self.elements['magiceden']['phantomWallet'])
        phantomExtension.click()

        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))

        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.elements['magiceden']['popup']['connectButton'])))
        popup = driver.find_element(By.XPATH, self.elements['magiceden']['popup']['connectButton'])
        popup.click()
        driver.switch_to.window(driver.window_handles[0])
        print("Done\n")

    def makePurchase(self, driver, url):
        print('Making purchase...')

        driver.get(url)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.elements['magiceden']['buyButton'])))
        driver.find_element(By.XPATH,self.elements['magiceden']['buyButton']).click()

        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.elements['magiceden']['popup']['approveButton'])))
        driver.find_element(By.XPATH, self.elements['magiceden']['popup']['approveButton']).click()

        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(1))
        time.sleep(5)
        print('Done\n')
