from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDriver(WebDriver):
    def __init__(self):
        options = Options()
        options.headless = True
        super().__init__(options=options)
