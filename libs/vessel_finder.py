import json
import logging
import sys

from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.consts import PAGE_URL, TIMEOUT, Locators


class VesselFinder:
    """
    Class for accessing marinetraffic.com page.
    """

    def __init__(self) -> None:
        """
        Initialize chrome driver with headless mode.
        """
        self.options = Options()
        self.options.headless = True
        logging.debug("Initialising Chrome driver.")
        self.driver = webdriver.Chrome(options=self.options)
        logging.debug(f"Opening Chrome on page: {PAGE_URL}")
        self.driver.get(PAGE_URL)
        self.cookie_consent()

    def cookie_consent(self):
        """
        Accept cookies. If timeout exceeded, exit code 1.
        """
        logging.info("Accepting cookies.")
        try:
            element_present = EC.element_to_be_clickable(
                (By.XPATH, Locators.COOKIE_XPATH)
            )
            WebDriverWait(self.driver, TIMEOUT).until(element_present)
            self.driver.find_elements_by_xpath(Locators.COOKIE_XPATH)[0].click()
        except TimeoutException:
            logging.error("Timed out waiting for page to load.")
            sys.exit(1)

    def vessel_info(self, imo_number: int) -> dict:
        """
        Get real-time information about given vessel.
        :param imo_number: International Maritime Organization (IMO) number
        :return: dictionary with vessel info
        """
        logging.info(f"Collecting vessel '{imo_number}' data.")

        self.driver.get(f"{PAGE_URL}/ais/details/ships//imo:{imo_number}")

        element_present = EC.element_to_be_clickable((By.XPATH, Locators.SHIP_XPATH))
        WebDriverWait(self.driver, TIMEOUT).until(element_present)

        page = etree.HTML(self.driver.page_source)
        return json.loads(page.xpath(Locators.SHIP_DATA)[-1].replace("  ", ""))

    def close_page(self) -> None:
        """
        Close chrome driver.
        """
        logging.info("Closing page.")
        self.driver.close()
