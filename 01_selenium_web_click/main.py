from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.get('https://www.anerbarrena.com/demos/2013/12-radio-button-jquery-demo2.php')

radio_btn = driver.find_element(By.XPATH,'//input[@id="edad2"]')
# radio_btn = driver.find_element('xpath','//input[@id="edad2"]')
radio_btn.click()

send_btn = driver.find_element('id', 'boton')
send_btn.click()

alert = Alert(driver)
alert.accept()
 
#Hay una ventana para aceptar cookies que puede bloquear el procedimiento