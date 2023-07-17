from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

CHROME_DRIVER_PATH = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class ScrapePageContent:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)

    def pageContent(self, url):
        self.driver.get(url)

        accept_cookie_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
        accept_cookie_button.click()

        self.driver.execute_script('window.scrollBy(0, 3000);')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="listing-item-link"]')))

        response = self.driver.execute_script('return document.body.innerHTML')
        return response
