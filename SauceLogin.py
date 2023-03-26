from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Checklogin():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")

    def username_empty(self):
        time.sleep(5)

        if self.username.text == "" and self.password.text == "":
            loginButton = self.driver.find_element(By.ID, "login-button")
            loginButton.click()
            errormessage = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
            print(errormessage.text)
            time.sleep(5)
            errorclose = self.driver.find_element(By.CLASS_NAME,"error-button")
            errorclose.click()


    def password_empty(self):
        time.sleep(5)
        self.username.send_keys("alibora")
        if self.password.text == "":
            loginButton = self.driver.find_element(By.ID, "login-button")
            loginButton.click()
            errormessage = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
            print(errormessage.text)
            time.sleep(5)
            errorclose = self.driver.find_element(By.CLASS_NAME,"error-button")
            errorclose.click()

    def lock_user_login(self):
        time.sleep(5)
        self.username.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errormessage = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errormessage.text)
        time.sleep(5)
        errorclose = self.driver.find_element(By.CLASS_NAME,"error-button")
        errorclose.click()

    def correct_user_login(self):
        time.sleep(5)
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        get_url = self.driver.current_url
        if str(get_url) ==  "https://www.saucedemo.com/inventory.html":
            checkproductcount = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
            if len(checkproductcount) == 6:
                print(len(checkproductcount))


def main():
    test = Checklogin()
    #test.username_empty()
    #test.password_empty()
    #test.lock_user_login()
    test.correct_user_login()
    while True:
        continue

if __name__=='__main__':
    main()
