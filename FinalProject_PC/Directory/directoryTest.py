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


class TestDirectory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_updateStatus(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory")

        time.sleep(3)

        name = "Rebecca Harmony"
        driver.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys(name)
        driver.find_element(By.ID,"searchBtn").click()

        time.sleep(3)
        result_name = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[1]/b").text

        self.assertEqual(name,result_name)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()