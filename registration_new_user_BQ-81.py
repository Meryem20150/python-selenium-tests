from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

breakpoint()

# Navigate to website
driver = webdriver.Chrome()
driver.get("http://dev.bootcamp.store.supersqa.com/")

# Click on "My Account"
my_account_link = driver.find_element(By.LINK_TEXT, "My Account")
my_account_link.click()

# Fill in the registration form
email_input = driver.find_element(By.ID, "reg_email")
password_input = driver.find_element(By.ID, "reg_password")
email_input.send_keys("m.meryembal@gmail.com")
password_input.send_keys("L@inaB1234567")

# Submit the registration form
register_button = driver.find_element(By.NAME, "register")
register_button.click()

# Wait for registration to complete
try:
    WebDriverWait(driver, 10).until(EC.url_contains("my-account"))
    print("User successfully registered!")
except:
    print("Registration failed or took too long.")

# Close the browser
driver.quit()

