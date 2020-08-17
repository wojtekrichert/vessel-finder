from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

TIMEOUT = 20


def wait_for_page():
    try:
        element_present = EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), ' I ACCEPT ')]"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.marinetraffic.com/pl/ais/details/ships//imo:9458028")
        timeout = 5
        wait_for_page()
        element = driver.find_elements_by_xpath("//*[contains(text(), ' I ACCEPT ')]")[0].click()
        time.sleep(10)
    except Exception as e:
        raise
    finally:
        driver.close()
