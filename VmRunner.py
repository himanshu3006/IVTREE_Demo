import subprocess
import sys, paramiko
import time


def create_instance():
    #vm = subprocess.call('VBoxManage registervm /home/arifivtree/VirtualBox\ VMs/vasanth/vasanth.vbox', shell=True)
    vm_start = subprocess.call('VBoxManage startvm Jenkins --type headless', shell=True)
    time.sleep(70)
    copy = subprocess.Popen('scp -r .* himanshu@192.168.0.24:/home/himanshu/Demo/',shell=True,stdin=subprocess.PIPE)
    copy.stdin.write('ivtree123\n')
    time.sleep(60)
    copy.wait()

    print ".......Instance Created......."

def execute_test():

    hostname = "192.168.0.24"
    password = "ivtree123"
    #command = "sudo systemctl start xvfb.service; export DISPLAY=:1; cd Demo; sudo rm -rf; python runner.py -b (command_args.build_id)"
    command = "sudo systemctl start xvfb.service; export DISPLAY=:1; cd Demo; python runner.py;"
    #command = "pwd; ls"
    username = "himanshu"
    port = 22

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)

        client.connect(hostname, port=port, username=username, password=password)
        print ".......Test Execution Process Started and Running......."
        stdin, stdout, stderr = client.exec_command(command)
       
        while str(stdout.channel.exit_status_ready()) != "True" :
               print "OUTPUT:%s"%stderr.read()
               print "OUTPUT:%s"%stdout.read()
	#stdin, stdout, stderr = client.exec_command("cd; cd Demo; rm -rf l*")

    finally:
        print ".......Test Execution Process Finished......."
        vm_start = subprocess.call('VBoxManage controlvm Jenkins poweroff', shell=True)
        #vm_permission = subprocess.call('sudo chmod -R 777 /home/arifivtree/VirtualBox\ VMs/', shell=True)
        client.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Gluster ROBOT FRAMEWORK")
    parser.add_argument("-b", action="store", default="False", dest="build_id")
    command_args = parser.parse_args()

    print "...Hello..."
    # x= range(10)
    # for y in x:
    #    create_instance()
    #    execute_test()
    create_instance()
    execute_test()
