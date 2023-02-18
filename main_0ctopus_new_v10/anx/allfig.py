import socket ,os

from anx import api_mysql



c1="1"
k=["0"]
k1=["1"]
# print(k)
goog="/root/g00g"
pwd = os.path.dirname(os.path.realpath( __file__ ))
hostname_os=socket.getfqdn()


telrgram_text=[]
def init_stuff():
	# os.system("rm -rf __pycache__/  > /dev/null 2>&1")
	os.system("rm *.tar.gz  > /dev/null 2>&1")



visible_v=0

if "LOOKE3" in hostname_os:
	# print(hostname_os)
	visible_v=1


def read_current_acc_goo():
	with open(goog,'r') as file:
		lines = file.readlines()
		lines=lines[0].replace("\n","")
	return lines

# print(read_current_acc_goo())

g00g_id,g00g_acc= api_mysql.get_active_goo()
# print(g00g_acc)
# 
init_stuff()
print(" hostname_os : "+hostname_os+"\n API : "+g00g_acc)
print(pwd)