from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

try:
    driver.execute_script("document.getElementById('fixedban').style.display='none'")
    driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none'")
except:
    pass

driver.find_element(By.ID,"firstName").send_keys("Prem")
driver.find_element(By.ID, "lastName").send_keys("Prajapati")

wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
email_input.send_keys("prem@gmail.com")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys('9876543210')

driver.find_element(By.ID, "dateOfBirthInput").click()
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text("May")
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_value("2004")
driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--004']").click()

subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("English")
subject_input.send_keys(Keys.ENTER)


driver.find_element(By.XPATH, "//label[text()='Reading']").click()

upload_path = os.path.abspath("sample.png")  # place a file named 'sample.png' in same folder
driver.find_element(By.ID, "uploadPicture").send_keys(upload_path)

# Address
driver.find_element(By.ID, "currentAddress").send_keys("123 Testing Lane, QA City")


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

# Submit the form
driver.find_element(By.ID, "submit").click()

# Wait to observe result
time.sleep(5)

driver.quit()

