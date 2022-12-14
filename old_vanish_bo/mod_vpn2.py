############################################ IPVANISH

import os ,random ,subprocess,time 
import vpn_sql
import cnf_bvb

l05_00='l05_00'
retry_count=[]
log_vpn_too=[]
pwd="/root/VPN"

rnd_yek=["33goQfhs6hfDauLzafL5PErP:3hx1mG2twanKEfQYsMPBZ6aw"]

# cnf_bvb.counting_left()

def random_pass():
	os.system("ps aux | grep  openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	random_ads=random.choice(rnd_yek)
	cmmd="rm nord_pass.txt"
	# print(cmmd)
	os.system(cmmd)
	sspl_t=random_ads.split(":")
	v_user=sspl_t[0]
	v_paww=sspl_t[1]
	# os.system('cat '+pwd+'nord_pass.txt && service openvpn restart')
	with open("nord_pass.txt",'a') as fw:
		# writ_new=v_user+"\n"+v_paww
		fw.write(v_user+"\n"+v_paww)
	os.system("cat nord_pass.txt &&  sed -i '/^$/d' nord_pass.txt ")
	print("\n")








########################### VPN  #############################/N0RD/WORKING_CONFIG/
# pwd = os.path.dirname(os.path.realpath( __file__ ))


vpn_type=cnf_bvb.vpn_type
if "N" in vpn_type:
	file_list_1='NORD_list_1'
	vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
	typ0="N"


if "C" in vpn_type:
	file_list_1='NCH_list_1'
	vpn_folder=pwd+"/CHEAP_VPN/"
	typ0="C"

if "V" in vpn_type:
	file_list_1='VANISH_list_1'
	vpn_folder=pwd+"/conf/"
	typ0="V"
	


def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")
	# 	# for i in all_vpn_config_file:




all_vpn_config_file=os.listdir(vpn_folder)
file_vpn_dead=cnf_bvb.file_vpn_dead
p_vpn_dead=cnf_bvb.p_vpn_dead

##############################################################

def check_list_vpn_lengh():
	num_lines = sum(1 for line in open(file_list_1))
	if num_lines==0:
		creat_list_of_vpn()
	else:
		pass

##############################################################

def creat_list_of_vpn():
	with open(file_list_1,'w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")

##############################################################


def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines


################################################################################


def read_default_timezone():
	# def read_current_list_vpn():
	with open('/root/test707','r') as file:
		titi_zon = file.readlines()
		titi_zon=titi_zon[0].replace("\n","")
		# print(titi_zon)
	return titi_zon
# read_default_timezone()

##############################################################



def read_pass():
	# def read_current_list_vpn():
	with open('pass_ipvan','r') as file:
		lines = file.readlines()
	return lines
##############################################################

def write_new_list(new_vpn_arry):
	with open(file_list_1,"w") as fw:
		for i in new_vpn_arry:
			fw.write(i)
	print("OK !!")

##############################################################

def remove_from_list_running(vpn_name):
	print("REMOVING THE VPN CONFIG [ "+vpn_name+" ]",end=' ',flush=True)
	vpn_name=vpn_name+"\n"
	arry_vpn_list=read_current_list_vpn()
	arry_vpn_list.remove(vpn_name)
	write_new_list(arry_vpn_list)

##############################################################



def get_random_vpn():
	fresh_config,int_used=vpn_sql.get_fresh_config(typ0)
	print(fresh_config,int_used)
	# check_list_vpn_lengh()
	# arry_vv=read_current_list_vpn()
	# random_vpn=random.choice(arry_vv)
	random_vpn=fresh_config
	final_vpn=vpn_folder+random_vpn
	# print(random_vpn)
	log_vpn_too.extend((final_vpn, random_vpn,int_used))
	return final_vpn , random_vpn ,int_used ,log_vpn_too

##############################################################

def change_time_zon(t_z):
	# t_z=get_time_zon()
	# print("Changing Time Zone ", end="")
	x = subprocess.Popen(['timedatectl', 'set-timezone', t_z])
	# print('OK'+t_z)
	time.sleep(3)

def fnc_vpn():
	print("################################  FNC_VPN  ###################################")
	os.system("echo '' > /var/log/openvpn/openvpn.log")
	# print(log_vpn_too)
	final_vpn,random_vpn,int_used,log_vpn_too=get_random_vpn()
	# print("KILLING OPENVPN ....",end=' ')
	os.system("ps aux | grep  openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	def_tz=read_default_timezone()

	change_time_zon(def_tz)
	# print(str(len(retry_count)))

	# time.sleep(3)
	# os.system("rm -rf /var/log/openvpn/openvpn.log")
	time.sleep(3)
	# os.system("touch /var/log/openvpn/openvpn.log")
	# print ("OK !!!!!")
	print("\n"+final_vpn)
	print("STARTING VPN        : " , end="")
	# x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])

	x = subprocess.Popen(['openvpn', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])
	# remove_from_list_running(random_vpn)
	# print("["+random_vpn+"]" , end="")
	time.sleep(15)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:

		if logfile.read().find('Sequence Completed') !=-1:
			# print ("  OK !!!!!")
			ac_ip,tz,loc=cnf_bvb.iip()
			change_time_zon(tz)
			os.environ['TZ'] = tz
			bass=read_pass()
			def_titi=read_default_timezone()
			print ("[ OK ]")
			mm=""
			for i in bass:
				mm=mm+i
			meddas=mm+def_titi+" [ CONNECTED VPN] [ "+str(int_used)+" ] : [ "+ random_vpn  +" ] \n"+"|| [ IP ] : [ "+ ac_ip+" ] || [ TIME_Z ] : ["+ tz+" ]"+"\n"
			# " [ "+url_1+" ]"
			append_to_l0g(meddas)
			vpn_sql.update_to_db_as_used(random_vpn,typ0)
			# print(meddas)
			cnf_bvb.ap_2_l0g(meddas)
			cnf_bvb.alias_send_msg(meddas)
			# print ("  OK !!!!!")
			print("VPN     CONFIG      : [ "+random_vpn+" ]")
			print("HOST    IP          : [ "+ac_ip+" ]")
			print("VPN     LOCATION    : [ "+loc+" ]")
			print("VPN     TIMEZONE    : [ "+tz+" ]")

			return [x ,True]
		if logfile.read().find('AUTH_FAILED'):
			print("\nAUTH_FAILED")
			os.system("echo '' > /var/log/openvpn/openvpn.log")
			# random_pass()

			retry_count.append("")
			if len(retry_count) ==4:
				cnf_bvb.alias_send_msg("AUTH_FAILED")

			print(str(len(retry_count)))
			time.sleep(3)
			x.kill()
			fnc_vpn ()
			return [x ,False]


		else :
			print("")
			print("VPN STATUS = OFF || "+ random_vpn )
			os.system("service openvpn restart")
			fnc_vpn ()
			return [x ,False]


	time.sleep(5)
	os.system("echo '' > /var/log/openvpn/openvpn.log")



	

########################################################################################################################################


################################
# fnc_vpn()
# get_random_vpn()
#cnf_bvb.testt()
# fnc_vpn ()
# get_random_vpn()