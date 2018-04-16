
from robot import run_cli
from robot import run
from robot.libraries import BuiltIn
import os
#################### 
from robot import run
import datetime

def run_robot(nightly='False',build_id=''):
   	"""This method used to run the robot framework both test and Contiouns integartion setup """
	if not nightly:
		now = str(datetime.datetime.now())
		test_run_folder="Robot_Logs"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

		complete_dir_path = os.path.join(os.getcwd(), "logs" + os.sep + test_run_folder)
		os.environ["RESULTS_PATH"]="%s"%test_run_folder
	
		if not os.path.isdir(complete_dir_path):
    			os.mkdir(complete_dir_path)
		else:
    			pass
		#Export the result directory for the test suite
		os.environ["RESULTS_PATH"]=test_run_folder


	else:
               complete_dir_path=os.path.join(os.getcwd(), "logs" + os.sep + build_id)
               os.environ["RESULTS_PATH"]="%s"%build_id
	       if not os.path.isdir(complete_dir_path):
                        os.mkdir(complete_dir_path)
               else:
                        pass

	#Form complete path to store html rport
        if nightly:
	
		complete_report_path= os.path.join(complete_dir_path,"report.html")
		#Form complete path to store log report
		complete_log_path=os.path.join(complete_dir_path,"log.html")
                complete_xml_path=os.path.join(complete_dir_path,"output.xml")
         
	else:
                complete_report_path= os.path.join(complete_dir_path,"Functional_"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".html")
                #Form complete path to store log report
                complete_log_path=os.path.join(complete_dir_path,"Functional_log"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".html")
     
	if not nightly:
		#start the suite
		run(	"resource/Gluster.robot",
    			 report=complete_report_path,log=complete_log_path)
	else:
		run(
	          	# "resource/Login/LoginToWizr.robot",
		        # "resource/camera/createDelete_Camera.robot",
                        "resource/Gluster.robot",
	                 report=complete_report_path,log=complete_log_path,output=complete_xml_path)
	


	#	run("resource/Login/LoginToWizr.robot",
	#	        "resource/Incident_Mangement/Inc_Man_1.robot",
        #                "resource/camera/createDelete_Camera.robot",
	#		report=complete_report_path,log=complete_log_path,output=complete_xml_path)




if __name__ == '__main__':
      import argparse
      parser=argparse.ArgumentParser(description="IVTREE ROBOT FRAMEWORK")
      parser.add_argument("-b",action="store",default="False",dest="build_id")
      command_args=parser.parse_args()
      if command_args.build_id:
      	 run_robot('True',command_args.build_id)
 
      else:
          
         run_robot()
                   




