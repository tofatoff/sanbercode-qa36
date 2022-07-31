import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase):
    
    url = "https://opensource-demo.orangehrmlive.com/"
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_successLogin_clickButton(self): 
        # steps
        global url
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(5)

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        actual_current_url = driver.current_url
        self.assertEqual(expected_current_url,actual_current_url)
        
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()