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


class TestEmployeeList(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_searchEmployee(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")

        time.sleep(3)

        expected_employeeName = "Cecil Bonaparte"
        expected_supervisorName = "Fiona Grace"
        expected_id = "0204"

        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(expected_employeeName)
        driver.find_element(By.ID, "empsearch_id").send_keys(expected_id)
        select_status = Select(driver.find_element(By.ID, "empsearch_employee_status"))
        select_status.select_by_visible_text("All")
        select_include = Select(driver.find_element(By.ID, "empsearch_termination"))
        select_include.select_by_visible_text("Current Employees Only")
        driver.find_element(By.ID, "empsearch_supervisor_name").send_keys(expected_supervisorName)
        select_jobTitle = Select(driver.find_element(By.ID, "empsearch_job_title"))
        select_jobTitle.select_by_visible_text("All")
        select_subUnit = Select(driver.find_element(By.ID, "empsearch_sub_unit"))
        select_subUnit.select_by_visible_text("All")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi
        result_id = driver.find_element(By.XPATH, "//*[@id=\"resultTable\"]/tbody/tr/td[2]/a").text
        # result_employeeName = driver.find_element(By.XPATH,"//*[@id=\"resultTable\"]/tbody/tr/td[3]/a").text + " " + driver.find_element(By.XPATH, "//*[@id=\"resultTable\"]/tbody/tr/td[4]/a")
        # result_supervisorName = driver.find_element(By.XPATH, "//*[@id=\"resultTable\"]/tbody/tr/td[8]").text

        self.assertEqual(expected_id, result_id)
        # self.assertEqual(expected_employeeName, result_employeeName)
        # self.assertEqual(expected_supervisorName, result_supervisorName)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()