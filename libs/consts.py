from dataclasses import dataclass

TIMEOUT = 20
PAGE_URL = "https://www.marinetraffic.com/pl"


@dataclass
class Locators:
    """
    Class for collecting all Selenium locators
    """

    COOKIE_XPATH: str = "//*[contains(text(), 'AGREE')]"
    SHIP_DATA: str = "//script[@type='application/ld+json']/text()"
    SHIP_XPATH: str = "//*[contains(text(), 'IMO: ')]"
