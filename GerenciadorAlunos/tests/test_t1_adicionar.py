# TESTE PARA ADICIONAR UM ALUNO 

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

LINK_ADICIONAR_ALUNO = (By.LINK_TEXT, "Adicionar Aluno")
CAMPO_NOME = (By.ID, "nome")
CAMPO_NOTA1 = (By.ID, "nota1")
CAMPO_NOTA2 = (By.ID, "nota2")
CAMPO_NOTA3 = (By.ID, "nota3")
CAMPO_NOTA4 = (By.ID, "nota4")
BOTAO_SUBMETER = (By.CSS_SELECTOR, ".btn:nth-child(6)")
LINK_EXCLUIR = (By.LINK_TEXT, "Excluir")

class TesteAdicionar:
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.wait = WebDriverWait(self.driver, 10) # Timeout
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adicionar_aluno(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1920, 1048)

    self.wait.until(EC.element_to_be_clickable(LINK_ADICIONAR_ALUNO)).click()
    self.wait.until(EC.element_to_be_clickable(CAMPO_NOME)).click()
    self.driver.find_element(*CAMPO_NOME).send_keys("Ana")
    self.wait.until(EC.element_to_be_clickable(CAMPO_NOTA1)).click()
    self.driver.find_element(*CAMPO_NOTA1).send_keys("7")
    self.driver.find_element(*CAMPO_NOTA2).send_keys("8")
    self.driver.find_element(*CAMPO_NOTA3).send_keys("6.5")
    self.driver.find_element(*CAMPO_NOTA4).send_keys("9")
    self.wait.until(EC.element_to_be_clickable(BOTAO_SUBMETER)).click()
    self.wait.until(EC.element_to_be_clickable(LINK_EXCLUIR)).click()
    
    self.wait.until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Tem certeza?"
    self.driver.switch_to.alert.accept()
