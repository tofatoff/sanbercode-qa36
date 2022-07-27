import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_successLogin_clickButton(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_current_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(expected_current_url,driver.current_url)
        
    def test_b_successLogin_pressEnter(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(1)

        # validasi
        expected_current_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(expected_current_url,driver.current_url)
        
    def test_c_failedLogin_wrongPassword(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("wrongpassword")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(expected_message,actual_message)
        
    def test_d_failedLogin_wrongUsername(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("wrongusername")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(expected_message,actual_message)
        
    def test_e_failedLogin_blankUsername(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username is required"
        actual_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(expected_message,actual_message)
        
    def test_f_failedLogin_blankPassword(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Password is required"
        actual_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(expected_message,actual_message)
    
    def test_g_failedLogin_blankUsernamePassword(self): 
        # steps
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        expected_message = "Epic sadface: Username is required"
        actual_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(expected_message,actual_message)
        
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()