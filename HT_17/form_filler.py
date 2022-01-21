"""
Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
заповнити і відправити її.
Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
В репозиторії скріншоти зберегти.
Корисні посилання:
https://www.selenium.dev/documentation/
https://chromedriver.chromium.org/downloads
"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = Chrome()
options = ChromeOptions()
options.add_argument('--headless')
browser.get('https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link')
text_field = browser.find_element(By.CLASS_NAME, 'exportInput')
text_field.click()
text_field.send_keys('Валентин Головко')
browser.save_screenshot('filled_form.png')
submit_button = browser.find_element(By.CSS_SELECTOR, 'span.exportLabel')
submit_button.click()
browser.save_screenshot('submitted_form.png')
