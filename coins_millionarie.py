from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

class CoinsMillionaire:
    def __init__(self):
        self.SITE_LINK = "https://www.ea.com/pt-br/ea-sports-fc/ultimate-team/web-app/"
        self.SITE_MAP  = {
            'buttons' : {
                'login' : {
                    "xpath" : "/html/body/main/div/div/div/button[1]"
                }
            }
        }
        self.SITE_EMAIL = 'diogouber@hotmail.com'
        self.SITE_PASS  = 'Derc6u4u6*' 
        service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def validar_login_ativo(self):
        self.driver.find_element(By.XPATH,self.SITE_MAP["buttons"]["login"]["xpath"]).click()

    def login(self):
        pass

coins = CoinsMillionaire()
coins.abrir_site()