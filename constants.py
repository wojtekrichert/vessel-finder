from dataclasses import dataclass

TIMEOUT = 20
SHIP_URL = "https://www.marinetraffic.com/pl/ais/details/ships//"


@dataclass(init=False)
class Locators:
    """
    Class for collecting all Selenium locators in one place
    """
    COOKIE_XPATH: str = "//*[contains(text(), ' I ACCEPT ')]"
    SHIP_DATA: str = "//script[@type='application/ld+json']/text()"
