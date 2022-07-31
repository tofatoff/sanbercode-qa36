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


class TestTime(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_searchEmployeeTimesheet(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/time/viewEmployeeTimesheet")

        time.sleep(3)

        name = "Cecil Bonaparte"
        driver.find_element(By.ID, "employee").click()
        driver.find_element(By.ID,"employee").send_keys(name)
        driver.find_element(By.ID,"btnView").click()

        time.sleep(3)
        result_name = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[1]/h3").text

        self.assertIn(name,result_name)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()