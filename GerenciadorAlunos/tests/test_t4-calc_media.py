# TESTE DE CÁLCULO DE MÉDIA

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

class TesteMedia():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.wait = WebDriverWait(self.driver, 10) # Timeout
    self.vars = {}
  
  def teardown_method(self, method):
    time.sleep(4)
    self.driver.quit()
  
  def test_media_nota(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1920, 1048)

    # Adicionar aluno
    self.wait.until(EC.element_to_be_clickable(LINK_ADICIONAR_ALUNO)).click()
    self.wait.until(EC.element_to_be_clickable(CAMPO_NOME)).click()
    self.driver.find_element(*CAMPO_NOME).send_keys("Ana")
    self.wait.until(EC.element_to_be_clickable(CAMPO_NOTA1)).click()
    self.driver.find_element(*CAMPO_NOTA1).send_keys("7")
    self.driver.find_element(*CAMPO_NOTA2).send_keys("7")
    self.driver.find_element(*CAMPO_NOTA3).send_keys("7")
    self.driver.find_element(*CAMPO_NOTA4).send_keys("7")
    self.wait.until(EC.element_to_be_clickable(BOTAO_SUBMETER)).click()
    
    # Verificar média (você precisará adicionar um seletor para a coluna de média)
    SELETOR_MEDIA = (By.XPATH, "//td[contains(text(), '7.0')]") 
    media_element = self.wait.until(EC.presence_of_element_located(SELETOR_MEDIA))

    # Se o teste falhar. Mostrar no terminal
    assert media_element.text == "7.0", f"Média esperada: 7.0, Média obtida: {media_element.text}"

    # Se o teste passar. Mostrar no terminal
    print("✅ Teste de média passou! A média foi calculada corretamente como 7.0")
    
    # Limpeza arquivo alunos.json
    self.wait.until(EC.element_to_be_clickable(LINK_EXCLUIR)).click()
    self.wait.until(EC.alert_is_present())
    self.driver.switch_to.alert.accept()