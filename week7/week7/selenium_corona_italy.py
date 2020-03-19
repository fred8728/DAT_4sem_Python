from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Brug selenium til at søge over italiens statistik over Corona 

def get_info(name):
    base_url = 'https://www.worldometers.info/coronavirus/?fbclid=IwAR05QM6HBBjgFkcthylUgtLxEPVxxfIhcAFHUEMZIPN9rnCzbrYC_HzwW0Q'
    browser = webdriver.Chrome()
    browser.get(base_url)
    browser.implicitly_wait(3)

    link_to_italy = browser.find_elements_by_link_text(name)
    link_to_italy[0].click()

    sleep(3)

    page_source = browser.page_source

get_info('Italy')