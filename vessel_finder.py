import logging
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from constants import Locators, TIMEOUT


class VesselFinder:
    """
    Class accessing data from .
    """
    def __init__(self):
        """
        Initialize chrome driver with headless mode.
        """
        self.options = Options()
        self.options.headless = True
        logging.debug("Initialising chrome driver.")
        self.driver = webdriver.Chrome(options=self.options)

    @classmethod
    def run(cls, imo_number):
        vessel_finder = VesselFinder()
        try:
            vessel_finder.vessel_info(imo_number)
        except Exception:
            raise
        finally:
            vessel_finder.close_page()

    def cookie_consent(self):
        """
        Find and accept cookies consent.
        """
        logging.info("Accepting cookies.")
        try:
            element_present = EC.element_to_be_clickable((By.XPATH, Locators.COOKIE_XPATH))
            WebDriverWait(self.driver, TIMEOUT).until(element_present)
            self.driver.find_elements_by_xpath(Locators.COOKIE_XPATH)[0].click()
        except TimeoutException:
            logging.error("Timed out waiting for page to load.")
            sys.exit(1)

    def vessel_info(self, imo_number: int):
        """
        Get real-time information about given vessel.
        :param imo_number: International Maritime Organization (IMO) number
        :return: dictionary with vessel info
        """
        logging.info("Opening marinetraffic.com page.")
        self.driver.get(f"https://www.marinetraffic.com/pl/ais/details/ships//imo:{imo_number}")
        self.cookie_consent()

    def close_page(self):
        """
        Close chrome driver.
        """
        logging.info("Closing page.")
        self.driver.close()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    VesselFinder.run(9458028)
