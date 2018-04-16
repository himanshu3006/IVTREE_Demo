#  Copyright 2017-2018 WiZR
#
#  Licensed under the  License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

#Automatic build trigger
from robot import run_cli
from robot import run
from robot.libraries import BuiltIn
import os
from robot import run
import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom
import pprint
import pdb
import json
import urllib
import urllib2
import telnetlib
import types
import commands
import string
import traceback
import copy
from robot.api import ExecutionResult
import unittest
from  testLinkLibrary import *
from robot.api import ExecutionResult, SuiteVisitor

def run_robot(nightly='False', build_id=''):
    import os
    """This method used to run the robot framework both test and Contiouns integartion setup """

    if not nightly:
        now = str(datetime.datetime.now())
        test_run_folder = "Robot_Logs" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        complete_dir_path = os.path.join(os.getcwd(), "logs" + os.sep + test_run_folder)
        os.environ["RESULTS_PATH"] = "%s" % test_run_folder

        if not os.path.isdir(complete_dir_path):
            os.mkdir(complete_dir_path)
        else:
            pass
        # Export the result directory for the test suite
        os.environ["RESULTS_PATH"] = test_run_folder


    else:
        complete_dir_path = os.path.join(os.getcwd(), "logs" + os.sep + build_id)
        os.environ["RESULTS_PATH"] = "%s" % build_id
        if not os.path.isdir(complete_dir_path):
            os.mkdir(complete_dir_path)
        else:
            pass

    # Form complete path to store html rport
    if nightly:

        complete_report_path = os.path.join(complete_dir_path, "report.html")
        # Form complete path to store log report
        complete_log_path = os.path.join(complete_dir_path, "log.html")
        complete_xml_path = os.path.join(complete_dir_path, "output.xml")

    else:
        complete_report_path = os.path.join(complete_dir_path,
                                            "Functional_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".html")
        # Form complete path to store log report
        complete_log_path = os.path.join(complete_dir_path,
                                         "Functional_log" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".html")

    if not nightly:
        # start the suite

        run(
            "resource/HomePage_IVtree.robot",
            report=complete_report_path, log=complete_log_path)
    else:
        import subprocess
        import os
        run("resource/HomePage_IVtree.robot",
            report=complete_report_path, log=complete_log_path, output=complete_xml_path)
        # run(
        #     "resource/HomePage_IVtree.robot",
        #     report=complete_report_path, log=complete_log_path, output=complete_xml_path)complete_xml_path
        return


#JustaComment
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


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="IVTREE ROBOT FRAMEWORK")
    parser.add_argument("-b", action="store", default="False", dest="build_id")
    command_args = parser.parse_args()
    try:

        if command_args.build_id:
            print "running"
            run_robot('True',command_args.build_id)
        else:
            run_robot()

    finally:
        print "finally"
        complete_dir_path = os.path.join(os.getcwd(), "logs" + os.sep + command_args.build_id)
        complete_xml_path = os.path.join(complete_dir_path, "output.xml")
        print complete_xml_path
        result = ExecutionResult(complete_xml_path)
        result.suite.visit(PrintTestInfo(command_args.build_id))












