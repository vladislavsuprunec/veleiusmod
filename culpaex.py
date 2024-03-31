from selenium.webdriver.common.by import By

bot_to_leave = driver.find_element(By.XPATH, f'//h4[contains(text(), "{bot}")]')
