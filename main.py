
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



browser = webdriver.Chrome()
browser.get('https://www.dns-shop.ru/')


search = browser.find_element_by_xpath("//*[@id='null']")
search.send_keys('logitech g102')
search.send_keys(Keys.ENTER)


product = browser.find_element_by_xpath("//*[@id='search-results']/div[1]/div[1]/div[1]/div[1]/div[4]/button[2]")
product.click()
product_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div/div[2]/a"
time.sleep(2)
def check_basket(xpath):
    basket = browser.get('https://www.dns-shop.ru/order/begin/')
    try:
        product_on_backet = browser.find_element_by_xpath(xpath)
        return print("товар найден")
    except:
        return print("товар не найден")

check_basket(product_xpath)