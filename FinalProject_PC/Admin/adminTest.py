from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Login.login import TestLogin

class TestAdmin(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_searchUser(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")
        
        time.sleep(3)
        
        expected_employeeName = "Cecil Bonaparte"
        expected_supervisorName = "Fiona Grace"
        expected_id = "0204"

        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys(expected_employeeName)
        driver.find_element(By.ID, "empsearch_id").send_keys(expected_id)
        select_status = Select(driver.find_element(By.ID,"empsearch_employee_status"))
        select_status.select_by_visible_text("All")
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(5)

        # validasi
        actual_username = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        actual_employeeName = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[4]").text
        self.assertEqual(expected_username,actual_username)
        self.assertEqual(expected_employeeName,actual_employeeName)
        
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()