from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver tanımlanır
driver.maximize_window()
#ekranı tam ekran yapar
driver.get("https://www.google.com")
#google ana sayfasına gidilir
time.sleep(1)

input = driver.find_element(By.NAME,"q") #google da HTML e name q ile gönderilmiş
#By.NAME ile "q" olan element i bul demek bu kod
input.send_keys("kodlamaio")
click = driver.find_element(By.NAME,"btnK")
time.sleep(1)
click.click()

firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()

listofcourse = driver.find_elements(By.CLASS_NAME,"course-listing")
print(len(listofcourse))
while True:
    continue
#-----------------HTML locators---------------

#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/div
#fullXpath kopyası en baştan kopyaladığımız yere kadar konumunu gösterir
#ancak HTML de araya div eklenirse fullXpath de değişiklik olacaktır

#//*[@id='rso']/div[1]/div/div/div[1]/div/a/div/div/div
#Xpath kopyası
#find_element içerisinde olduğu için rso yu tek tırnakta tutarız
#id si rso olandan itibaren div leri yazar