import threading
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CustomLibrary(object):
    
    def async_close_browser(self):
        """
        Close the current browser asynchronous. It can save a few seconds.
        """
        t = threading.Thread(target = lambda: BuiltIn().get_library_instance('SeleniumLibrary').close_browser())
        t.start()

    def set_headless_options(self, width=1920, height=1080):
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--window-size=%s,%s" % (width, height))
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("--ignore-certificate-errors")
        chromeOptions.add_argument("--allow-running-insecure-content")
        chromeOptions.add_argument("--log-level=3")
        return chromeOptions

    def accept_insecure_certs(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        return capabilities
