import subprocess  
#p = subprocess.check_output('ls -l', shell=True)
#(stdout, stderr) = p.communicate()

#exit_code = p.returncode
a = u'ps -ef | grep process'
commands = [u'df -h' , u'ls -ltr' , u'ps -ef | grep process', u'ls']

task = [command for command in commands if a == command]

print task
