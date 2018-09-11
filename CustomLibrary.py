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

    def set_headless_options(self, width=1920, height=1080, options=None):
        if not options:
            options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=%s,%s" % (width, height))
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        return options
    
    def change_log_level(self, level=3, options=None):
        if not options:
            options = Options()
        options.add_argument("--log-level=3")
        return options

    def accept_insecure_certs(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        return capabilities
