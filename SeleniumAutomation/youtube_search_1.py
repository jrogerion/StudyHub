from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

''' Código para automatizar a realização de um pesquisa simples no YOUTUBE usando o FIREFOX'''

browser = webdriver.Firefox()
browser.maximize_window()

try:
    browser.get('https://www.youtube.com')

    # Caixa de pesquisa
    seach_box = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytSearchboxComponentInput'))
    ) 
    # Botão de pesquisa
    seach_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytSearchboxComponentSearchButton'))
    )

    # Fazendo a pesquisa
    seach_box.send_keys('automação+selenium')
    seach_button.click()
    sleep(5)

    # Limpando caixa de pesquisa
    seach_box.clear()

    # Realizando outra pesquisa
    seach_box.send_keys('curso+python')
    seach_button.click()
    sleep(5)

finally:
    browser.quit()
