import threading
from robot.libraries.BuiltIn import BuiltIn


class CustomLibrary(object):
    
    def async_close_browser(self):
        """
        Close the current browser asynchronous. It can save a few seconds.
        """
        t = threading.Thread(target = lambda: BuiltIn().get_library_instance('SeleniumLibrary').close_browser())
        t.start()
