from pages.WebGeneric import WebGeneric
from data.testdata import *
class Login(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self,driver)
        self.driver = driver
        self.signin_nav="//a[text()='Sign In']"
        self.un_id="email"
        self.pwd_id="password"
        self.Sign_in="btnSignin"
        self.wg = WebGeneric(self.driver)

    def zoomin_login(self):
        self.wg.signin("xpath",self.signin_nav)
        self.wg.enter("id", self.un_id, USERNAME)
        self.enter("id", self.pwd_id, PASSWORD)
        self.submit("id",self.Sign_in)

        # Login to the application
        # self.driver.find_element_by_xpath("//a[text()='Sign In']").click()
        # self.driver.find_element_by_xpath("//input[@placeholder='Email or Username']").send_keys(un)
        # self.driver.find_element_by_id("password").send_keys(pwd)
        # self.driver.find_element_by_id("btnSignin").click()
