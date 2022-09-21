class BasePageClass:
    
    _URL = None

    def go(self):
        #add wait for page loading
        self.driver.get(self._URL)