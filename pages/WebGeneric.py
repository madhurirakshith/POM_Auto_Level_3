from pages.LocatorGeneric import LocatorGeneric
class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)

    def signin(self, locator_type,locator_val):
        var = self.locator(locator_type, locator_val)
        var.click()

    def enter(self, locator_type,locator_val, input_val):
        var = self.locator(locator_type, locator_val)
        var.send_keys(input_val)

    def submit(self, locator_type,locator_val):
        var = self.locator(locator_type, locator_val)
        var.click()
