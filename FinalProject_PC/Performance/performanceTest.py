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


class TestPerformance(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_searchKPI(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/performance/searchKpi")

        time.sleep(3)

        expected_jobTitle = "QA Engineer"

        select_userRole = Select(driver.find_element(By.ID, "kpi360SearchForm_jobTitleCode"))
        select_userRole.select_by_visible_text(expected_jobTitle)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi
        table = driver.find_element(By.XPATH,"//*[@id=\"resultTable\"]/tbody")
        table_rows = table.find_elements(By.TAG_NAME,"tr")
        for row in table_rows:
            self.assertEqual(expected_jobTitle,row.find_elements(By.TAG_NAME,"td")[2].text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()