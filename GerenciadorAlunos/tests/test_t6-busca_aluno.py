# TESTE DE BUSCA DE ALUNOS

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TesteBuscaAluno():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 5) 
        self.driver.get("http://localhost:5000/")
        self.driver.maximize_window()
        time.sleep(0.5)  

    def teardown_method(self, method):
        time.sleep(1)  
        self.driver.quit()

    def slow_type(self, element, text, delay=0.1): 
        """Digita texto mais rapidamente"""
        for character in text:
            element.send_keys(character)
            time.sleep(delay)

    def fast_click(self, locator):
        """Clica em um elemento com espera mínima"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        time.sleep(0.3) 
        element.click()
        time.sleep(0.3)  

    def test_buscaraluno(self):
        alunos = [
            {"nome": "Maria", "notas": ["7", "7", "7", "7"]},
            {"nome": "Jose", "notas": ["8", "8", "8", "8"]},
            {"nome": "Mario", "notas": ["6.7", "6", "5", "8"]}
        ]

        for aluno in alunos:
            self.fast_click((By.LINK_TEXT, "Adicionar Aluno"))
            
            nome_field = self.driver.find_element(By.ID, "nome")
            nome_field.click()
            self.slow_type(nome_field, aluno["nome"])
            
            for i, nota in enumerate(aluno["notas"], start=1):
                nota_field = self.driver.find_element(By.ID, f"nota{i}")
                nota_field.click()
                nota_field.send_keys(nota) 
                time.sleep(0.2)  
            
            self.fast_click((By.CSS_SELECTOR, ".btn:nth-child(6)"))
            time.sleep(0.5)  

        buscas = ["maria", "maRIO", "JOOse", "jose"]
        self.fast_click((By.LINK_TEXT, "Buscar Aluno"))
        
        for termo in buscas:
            campo_busca = self.driver.find_element(By.ID, "nome")
            campo_busca.clear()
            campo_busca.send_keys(termo) 
            self.fast_click((By.CSS_SELECTOR, "form > .btn"))
            time.sleep(1) 

        for _ in range(3):
            self.fast_click((By.LINK_TEXT, "Início"))
            self.fast_click((By.LINK_TEXT, "Excluir"))
            
            alert = self.wait.until(EC.alert_is_present())
            assert alert.text == "Tem certeza?"
            time.sleep(0.5) 
            alert.accept()
            time.sleep(0.5) 