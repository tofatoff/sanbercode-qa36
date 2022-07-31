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


class TestBuzz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_updateStatus(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/buzz/viewBuzz")

        time.sleep(3)

        status_post = "Lorem ipsum dolor sit amet"

        driver.find_element(By.ID,"createPost_content").send_keys(status_post)
        time.sleep(1)
        driver.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(2)
        # statuses = driver.find_element(By.ID,"buzz")
        newest_status = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[6]/ul/li[1]/div[1]/div[5]/div").text
        self.assertEqual(newest_status,status_post)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()