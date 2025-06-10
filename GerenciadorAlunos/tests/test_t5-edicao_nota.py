# TESTE DE EDIÇÃO DE NOTAS

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class TesteEdicaoNota():
  def setup_method(self, method):

    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    time.sleep(2)
    self.driver.quit()
  
  def test_edita_(self):
    self.driver.get("http://localhost:5000/")
    self.driver.maximize_window()

    self.driver.find_element(By.LINK_TEXT, "Adicionar Aluno").click()
    self.driver.find_element(By.ID, "nome").click()
    self.driver.find_element(By.ID, "nome").send_keys("Jose")
    self.driver.find_element(By.ID, "nota1").send_keys("5")
    self.driver.find_element(By.ID, "nota2").click()
    self.driver.find_element(By.ID, "nota2").send_keys("5")
    self.driver.find_element(By.ID, "nota3").click()
    self.driver.find_element(By.ID, "nota3").send_keys("5")
    self.driver.find_element(By.ID, "nota4").click()
    self.driver.find_element(By.ID, "nota4").send_keys("5")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    self.driver.find_element(By.ID, "nova_nota").click()
    self.driver.find_element(By.ID, "nova_nota").send_keys("9")
    self.driver.find_element(By.CSS_SELECTOR, "form > .btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    self.driver.find_element(By.ID, "nota_numero").click()
    dropdown = self.driver.find_element(By.ID, "nota_numero")
    dropdown.find_element(By.XPATH, "//option[. = 'Nota 2 (Atual: 5.0)']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "nova_nota").click()
    self.driver.find_element(By.ID, "nova_nota").send_keys("8")
    self.driver.find_element(By.CSS_SELECTOR, "form > .btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    self.driver.find_element(By.ID, "nota_numero").click()
    dropdown = self.driver.find_element(By.ID, "nota_numero")
    dropdown.find_element(By.XPATH, "//option[. = 'Nota 3 (Atual: 5.0)']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
    self.driver.find_element(By.ID, "nova_nota").click()
    self.driver.find_element(By.ID, "nova_nota").send_keys("7")
    self.driver.find_element(By.CSS_SELECTOR, "form > .btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Editar").click()
    self.driver.find_element(By.ID, "nota_numero").click()
    dropdown = self.driver.find_element(By.ID, "nota_numero")
    dropdown.find_element(By.XPATH, "//option[. = 'Nota 4 (Atual: 5.0)']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
    self.driver.find_element(By.ID, "nova_nota").click()
    self.driver.find_element(By.ID, "nova_nota").send_keys("6")
    self.driver.find_element(By.CSS_SELECTOR, "form > .btn-primary").click()

    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Excluir").click()
    assert self.driver.switch_to.alert.text == "Tem certeza?"
    self.driver.switch_to.alert.accept()
  
