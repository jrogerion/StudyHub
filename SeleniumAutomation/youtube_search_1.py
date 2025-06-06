from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

''' Código para automatizar a realização de um pesquisa simples no YOUTUBE usando o FIREFOX'''

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.youtube.com')

search_box = browser.find_element(By.CSS_SELECTOR, '.ytSearchboxComponentInput')
search_box.click()
search_box.send_keys('atomação+selenium')

search_button = browser.find_element(By.CSS_SELECTOR, '.ytSearchboxComponentSearchButton')
search_button.click()
sleep(5)
search_box.clear()

# Outra pesquisa
search_box.click()
search_box.send_keys('curso+python')
search_button.click()
sleep(5)

browser.close()