from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_info(name):
    base_url = 'http://www.ikea.dk'
    browser = webdriver.Chrome()
    browser.get(base_url)
    browser.implicitly_wait(3)

    # search_field = browser.find_element_by_tag_name('input')
    search_field = browser.find_element_by_name('q')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)
    # browser.implicitly_wait(3)

    page_source = browser.page_source


get_info('skabe')