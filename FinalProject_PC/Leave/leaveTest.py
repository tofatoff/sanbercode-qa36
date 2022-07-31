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


class TestLeave(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_searchLeaveList(self):
        TestLogin.test_a_successLogin_clickButton(self)
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList")

        time.sleep(3)

        driver.find_element(By.ID,"calFromDate").click()
        time.sleep(1)
        datepicker_month = Select(driver.find_element(By.CLASS_NAME,"ui-datepicker-month"))
        time.sleep(1)
        datepicker_month.select_by_visible_text("Dec")
        time.sleep(1)
        datepicker_year = Select(driver.find_element(By.CLASS_NAME,"ui-datepicker-year"))
        time.sleep(1)
        datepicker_year.select_by_visible_text("2020")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[3]/table/tbody/tr[4]/td[1]/a").click()
        time.sleep(1)
        dateFrom = driver.find_element(By.ID,"calFromDate").get_attribute("value")

        driver.find_element(By.ID, "calToDate").click()
        time.sleep(1)
        datepicker_month = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
        time.sleep(1)
        datepicker_month.select_by_visible_text("Dec")
        time.sleep(1)
        datepicker_year = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
        time.sleep(1)
        datepicker_year.select_by_visible_text("2020")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[4]/td[3]/a").click()
        time.sleep(1)
        dateTo = driver.find_element(By.ID, "calToDate").get_attribute("value")

        check_all = driver.find_element(By.ID,"leaveList_chkSearchFilter_checkboxgroup_allcheck")
        if check_all.get_attribute("checked") != "checked":
            check_all.click()

        employee = "Rebecca Harmony"
        driver.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys(employee)

        select_subunit = Select(driver.find_element(By.ID, "leaveList_cmbSubunit"))
        select_subunit.select_by_visible_text("All")

        check_pastEmployee = driver.find_element(By.ID,"leaveList_cmbWithTerminated")
        if check_pastEmployee.get_attribute("checked") == "checked":
            check_pastEmployee.click()

        driver.find_element(By.ID, "btnSearch").click()
        time.sleep(5)

        # validasi
        result_date = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody/tr/td[1]/a").text
        result_employee = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody/tr/td[2]/a").text
        if dateFrom in result_date:
            self.assertIn(dateFrom,result_date)
        if dateTo in result_date:
            self.assertIn(dateTo,result_date)
        self.assertEqual(employee,result_employee)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()