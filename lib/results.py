from robot.api import ExecutionResult, SuiteVisitor
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
from  testLinkLibrary import *


class PrintTestInfo(SuiteVisitor):
    def __init__(self,jenkins_build=''):
        self.build=jenkins_build
        self.result = {}
        tree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'ConfigInput.xml')
        for node in tree.iter():
            if node.tag == "Parameters":
                self.result_dict = node.attrib
        self.tls = getTestLinkObject(
            self.result_dict['testLinkURL'], self.result_dict['testLinkDEVKEY'])
        addBuildToTestPlan(self.tls, self.result_dict['testLinkTestProjectName'], self.result_dict['testLinkTestPlanName'],
                           self.build, "fROM AUT")

    def visit_test(self, test):
        if test.status == "PASS":
            testCaseStatus = 'p'
        else:
            testCaseStatus = 'f'

        updateResultInTestLink(self.tls, self.result_dict['testLinkTestProjectName'], self.result_dict['testLinkTestPlanName'],
                               self.build, test.name.strip(":"),testCaseStatus, self.result_dict['testLinkPlatform'])





result = ExecutionResult('output.xml')
final=result.suite.visit(PrintTestInfo("mydsafwaf"))

#print result1

# if __name__ == '__main__':
#     print "HELLO RESULTS"
#     #results()
#     result.suite.visit()