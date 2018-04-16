from robotpageobjects import Page, robot_alias
from robot.api import logger
import time
from Utility import *

class IVTreeHomePage(Page):
    selectors = {
        "Home_menu": "xpath=(//a[contains(text(),'Home')])[1]",
        "Company_menu":"xpath=(//a[contains(text(),'Company')])[1]",
        "Your_email":"xpath=//input[contains(@name,'EMAIL')]",
        "Submit_button":"xpath=//input[contains(@value,'Send')]",
        "News_letter":"xpath=//div[contains(@class,'letter-title ')]",
        "Product_menu":"xpath=(//a[contains(text(),'Products')])[1]",
        "Click_sales":"xpath=//a[contains(text(),'sales@ivtree.com')]",
                #Client Area
        "client_menu":"xpath=(//a[contains(text(),'Client Area')])[1]",
        "userName_Login":"xpath=//input[contains(@id,'login-name')]",
        "password_Login":"xpath=//input[contains(@id,'login-pass')]",
        "Sigin_button":"xpath=//input[contains(@name,'login_submit')]",
        "SiginUp_Client":"xpath=//a[contains(text(),'Sign Up')]",

    }

    def __init__(self,*args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    def scroll__bar(self):
        '''
        scrolling of scroll-bar in a page
        :param text:
        :return:
        '''
        alert = None
        try:
            alert = self._current_browser().switch_to_alert()
            logger.info("scrolled ")
            return alert
            self.execute_javascript("current_prompt.scrollBy(0,450)")
            time.sleep(8)

        except:
            raise RuntimeError('There were no alerts')

    def Navigate_Between_HomeCompany(self, email):
        '''
        this functions helps to navigate between home and company module
        and passing emailID to get NewsLetter of product
        :param email:
        :return:
        '''
        self.click_element("Home_menu")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        self.click_element("Company_menu")
        second =range(0,5)
        for sec in second:
            if sec >= 5:
               break
            self.driver.execute_script("window.scrollBy(0,1500)", "")
            time.sleep(5)
        self.get_text("News_letter")
        self.input_text("Your_email",email)
        self.click_button("Submit_button")
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Navigation succesful", html=True)
        return self

    def Products_Module(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        self.click_element("Product_menu")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        self.click_element("Click_sales")
        # taking screenshot at last of operation
        #self.Utility_obj.takescreen()
        logger.info('Product modules succesfully clicked sales', html=True)
        return  self

    def Client_AreaModule(self, login, username, password):
        '''

        :return:
        '''
        self.click_element("client_menu")
        heading=self.get_title()
        self.title_should_be(title=heading)
        if login == 'Have Account':
            self.input_text("userName_Login",username)
            self.input_password("password_Login",password)
            self.click_element("Sigin_button")
        else:
            self.click_element("SiginUp_Client")

        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Client area developed", html=True)
        return self
    def Products_Module1_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        self.click_element("Product_menu")
        time.sleep(10)
        self.Utility_obj.takescreen()
        logger.info('Product modules 1 succesfully clicked sales', html=True)
        return  self
    def Products_Module2_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 2 succesfully clicked sales', html=True)
        return self

    def Products_Module3_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 3 succesfully clicked sales', html=True)
        return self

    def Products_Module4_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 4 succesfully clicked sales', html=True)
        return self

    def Products_Module5_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 5 succesfully clicked sales', html=True)
        return self

    def Products_Module6_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 6 succesfully clicked sales', html=True)
        return self

    def Products_Module7_test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Testing "
        # taking screenshot at last of operation
        logger.info('Product modules 7 succesfully clicked sales', html=True)
        return self

    def Product_Feature1_Test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Feature "
        # taking screenshot at last of operation
        logger.info('Product modules 2 succesfully clicked sales', html=True)
        return self

    def Product_Feature2_Test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Feature "
        # taking screenshot at last of operation
        logger.info('Product modules 2 succesfully clicked sales', html=True)
        return self

    def Product_Feature3_Test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Feature "
        # taking screenshot at last of operation
        logger.info('Product modules 2 succesfully clicked sales', html=True)
        return self

    def Product_Feature4_Test(self):
        '''
        THIS FUNCTIONS HELPS US TO GET SALES DETAILS OF PRODUCT
        :return:
        '''
        print "Product Feature "
        # taking screenshot at last of operation
        logger.info('Product modules 2 succesfully clicked sales', html=True)
        return self

    if __name__ == "__main__":
        Page.main()
