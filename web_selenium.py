from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

#Determinar la ruta
PATH='C:\Program Files (x86)\chromedriver.exe'
#Definir variable
driver=webdriver.Chrome(PATH)
#Para obtener la página
driver.get("https://carnetvacunacion.minsa.gob.pe/#/verify-qr/enable")
time.sleep(1)
codigoqr = driver.find_element_by_xpath('//*[@id="-body"]/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[4]/span[2]')
print(codigoqr.text)
driver.quit()
