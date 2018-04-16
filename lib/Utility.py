
# Importing classes for utilising current library
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
import os


class Utility():

    def takescreen(self):
        '''
           This functions help us to take screenShot curent page
           :param self:
           :param testcase_id:
           :return:
           '''
        self.testcase_id = BuiltIn().get_variable_value("${testcase_id}")
        results_path = os.path.join(os.getcwd(), "logs" + os.sep +
                                    os.environ["RESULTS_PATH"] + os.sep + "screenshots")

        if not os.path.exists(results_path):
            os.mkdir(results_path)
        else:
            pass
        #creating object of screenshot & passing the path where to store it
        screeobj = Screenshot(results_path)
        screeobj.take_screenshot(self.testcase_id)
        # return self

