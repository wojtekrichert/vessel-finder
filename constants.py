from dataclasses import dataclass

TIMEOUT = 20


@dataclass(init=False)
class Locators:
    """
    Class for collecting all Selenium locators in one place
    """
    COOKIE_XPATH: str = "//*[contains(text(), ' I ACCEPT ')]"
