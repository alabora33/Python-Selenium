from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Test_Kodlama():
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        time.sleep(5)
        username = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        time.sleep(5)
        username.send_keys("1")
        password.send_keys("1")
        time.sleep(5)
        login = driver.find_element(By.ID,"login-button")
        login.click()
        errormessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testresult = errormessage.text == "HATALI GİRİŞ"
        print(testresult)
        time.sleep(100)


testClass =Test_Kodlama()
testClass.test_invalid_login()





while True:
    continue