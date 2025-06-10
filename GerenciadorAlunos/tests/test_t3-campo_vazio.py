# TESTE AO INSERIR CAMPOS VAZIOS

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
import time

LINK_ADICIONAR_ALUNO = (By.LINK_TEXT, "Adicionar Aluno")
CAMPO_NOME = (By.ID, "nome")
CAMPO_NOTA1 = (By.ID, "nota1")
CAMPO_NOTA2 = (By.ID, "nota2")
CAMPO_NOTA3 = (By.ID, "nota3")
CAMPO_NOTA4 = (By.ID, "nota4")
BOTAO_SUBMETER = (By.CSS_SELECTOR, ".btn:nth-child(6)")
LINK_EXCLUIR = (By.LINK_TEXT, "Excluir")

class TesteCampoVazio:
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.wait = WebDriverWait(self.driver, 10) # Timeout
    self.vars = {}
  
  def teardown_method(self, method):
    time.sleep(0.5)
    self.driver.quit()
  
  def test_campos_vazios(self):
    self.driver.get("http://localhost:5000/")
    self.driver.maximize_window()
    
    campos_notas = [CAMPO_NOTA1, CAMPO_NOTA2, CAMPO_NOTA3, CAMPO_NOTA4]
    

    self.wait.until(EC.element_to_be_clickable(LINK_ADICIONAR_ALUNO)).click()
    time.sleep(0.5) 
        
    self.wait.until(EC.element_to_be_clickable(BOTAO_SUBMETER)).click()
    
    for campo_com_15 in campos_notas:
        time.sleep(0.5) 
        # Preenche nome
        self.wait.until(EC.element_to_be_clickable(CAMPO_NOME)).clear()
        self.driver.find_element(*CAMPO_NOME).send_keys("Pedro")
        time.sleep(0.5) 
        
        # Preenche notas
        for campo in campos_notas:
            if campo == campo_com_15:
                self.wait.until(EC.element_to_be_clickable(campo)).clear()
                self.driver.find_element(*campo).send_keys("")
            else:
                self.driver.find_element(*campo).clear()
                self.driver.find_element(*campo).send_keys("7")
            time.sleep(0.5)  
        
        # Submete o formulário
        self.wait.until(EC.element_to_be_clickable(BOTAO_SUBMETER)).click()
        time.sleep(0.5)  #