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
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewCandidates")

        time.sleep(3)

        name = "Garry White"

        Select(driver.find_element(By.ID,"candidateSearch_jobTitle")).select_by_visible_text("All")
        Select(driver.find_element(By.ID, "candidateSearch_jobVacancy")).select_by_visible_text("All")
        Select(driver.find_element(By.ID, "candidateSearch_hiringManager")).select_by_visible_text("All")
        Select(driver.find_element(By.ID, "candidateSearch_status")).select_by_visible_text("All")

        driver.find_element(By.ID,"candidateSearch_candidateName").send_keys(name)
        driver.find_element(By.ID,"candidateSearch_keywords").click()
        driver.find_element(By.ID, "candidateSearch_fromDate").click()
        driver.find_element(By.ID, "candidateSearch_toDate").click()

        Select(driver.find_element(By.ID, "candidateSearch_modeOfApplication")).select_by_visible_text("All")

        driver.find_element(By.ID,"btnSrch").click()

        time.sleep(3)
        result_name = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[3]").text

        self.assertIn(name,result_name)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()