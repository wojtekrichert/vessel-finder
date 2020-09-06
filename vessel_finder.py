import json
import logging
import sys

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from constants import Locators, TIMEOUT, SHIP_URL


class VesselFinder:
    """
    Class for accessing marinetraffic.com page.
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
            data = vessel_finder.vessel_info(imo_number)
            logging.info(data)
        except Exception:
            raise
        finally:
            vessel_finder.close_page()

    def cookie_consent(self):
        """
        Accept cookies.
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
        logging.info(f"Opening marinetraffic.com page with info about vessel: {imo_number}")
        self.driver.get(f"{SHIP_URL}imo:{imo_number}")
        self.cookie_consent()
        page = etree.HTML(self.driver.page_source)
        return json.loads(page.xpath(Locators.SHIP_DATA)[-1].replace("  ", ""))

    def close_page(self):
        """
        Close chrome driver.
        """
        logging.info("Closing page.")
        self.driver.close()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    VesselFinder.run(9458028)
