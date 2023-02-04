import  os
os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
os.system('rm -rf anx/__pycache__  > /dev/null 2>&1 &&  anx/ rm -rf /tmp/.*  > /dev/null 2>&1 && rm -rf /tmp/tmp* > /dev/null 2>&1')
os.system("clear")
print("Clean")
print("module loaded ")