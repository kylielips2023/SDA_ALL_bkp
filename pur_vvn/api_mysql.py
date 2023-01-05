import para_m


import requests
import json
#  ls ~/VPN/N0RD/WORKING_CONFIG | wc -l

api_url=para_m.url
# print(api_url)


#/////////////////////  get_config_with_api ///////////////////////////////////////////

def get_config_with_api_pure(i_d):
	response = requests.get(f"{api_url}/pure/%d" %i_d )

	data = response.json()
	data_id = data.get('id')
	data_cnf_names = data.get('cnf_names')
	data_used = data.get('used')
	print(data_id,data_cnf_names,data_used)
	return data_id,data_cnf_names,data_used


#////////////////////////////////////////////////////////////////
#//////// * VANISH * - count_left_api ////////////////////////////////////////////////////////
def pure_count_left_api():
	response = requests.get(f'{api_url}/pure/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)
	return count_left_count
#////////////////////////////////////////////////////////////////
# van_count_left_api()

# van_count_left_api()

#////////// * VANISH * get_random_api ///////////////////////////////////////////////////////////////

def get_random_api_pure():
	response = requests.get(f'{api_url}/pure/ran')
	data = response.json()
	print(data)
	data_id = data[0].get('id')
	data_cnf_names = data[0].get('cnf_names')
	data_used = data[0].get('used')
	pure_config_left=pure_count_left_api()
	print(data_id,data_cnf_names,data_used,pure_config_left)
	return data_id,data_cnf_names,data_used,pure_config_left
#////////////////////////////////////////////////////////////////
get_random_api_pure()

#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def update_conf_pure_api(id_config):
	pure_count_left_api()
	# print(id_config)
	get_config_with_api_pure(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/pure/update/%d" % id_config)
	print(response.content)
	get_config_with_api_pure(id_config)
	pure_count_left_api()
# update_conf_pure_api(185)
# pure_count_left_api()
get_config_with_api_pure(185)
#/////////////////////   ///////////////////////////////////////////  get_config_with_api

#/////////////////   /////////////////////////////////////////////// reset_van_api

def reset_pure_api():

	response = requests.put(f'{api_url}/pure/reset_all')
	data = response.json()
	data_message = data.get('message')
	# print(response.content)
	print(data_message)

#//////////////////////////////////////////////////////////////////////////////////////////////











#////////  Account Active ////////////////////////////////////////////////////////

def get_active_goo():
	response = requests.get(f'{api_url}/google_account_pure/active')
	data = response.json()
	data_id = data[0].get('acc_numbre')
	data_name_acc = data[0].get('account_id')
	print(data_id,data_name_acc)
	return data_id , data_name_acc
#////////////////////////////////////////////////////////////////
# get_active_goo()

# count_left_api()


#//////// * N0RD * - count_left_api ////////////////////////////////////////////////////////

def count_left_api():
	response = requests.get(f'{api_url}/nor/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)
	return count_left_count
#////////////////////////////////////////////////////////////////


#//////////  get_random_api ///////////////////////////////////////////////////////////////

def get_random_api():
	response = requests.get(f'{api_url}/nor/ran')

	data = response.json()
	data_id = data[0].get('id')
	data_cnf_names = data[0].get('cnf_names')
	data_used = data[0].get('used')

	return data_id,data_cnf_names,data_used
#////////////////////////////////////////////////////////////////


#/////////////////  reset_nord_api ///////////////////////////////////////////////
#////////////////
def reset_nord_api():

	response = requests.put(f'{api_url}/nor/reset_all')
	data = response.json()
	data_message = data.get('message')
	# print(response.content)
	print(data_message)

#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def update_conf_nord_api(id_config):
	count_left_api()
	# print(id_config)
	get_config_with_api(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/nor/update/%d" % id_config)
	# print(response.content)
	get_config_with_api(id_config)
	count_left_api()



#/////////////////////  get_config_with_api ///////////////////////////////////////////

def get_config_with_api(i_d):
	response = requests.get(f"{api_url}/nor/%d" %i_d )

	data = response.json()
	data_id = data.get('id')
	data_cnf_names = data.get('cnf_names')
	data_used = data.get('used')
	print(data_id,data_cnf_names,data_used)
	return data_id,data_cnf_names,data_used


#////////////////////////////////////////////////////////////////

def pure_check_tolerance():

	
	# count_used=str(counting_used_config_config())
	# print(" [  VPN USED  ]",type(count_used))
	count_used=pure_count_left_api()
	int_count=int(count_used)
	# print(" [  VPN USED  ]",type(int_count))
	
	if int_count >= 25 :
		print(int_count)
		print("NO Reset Count : "+str(int_count))
		# restored_fresh_sql_table()
	else :
		print(int_count)
		print(" Reset "+str(int_count))
		reset_pure_api()

pure_check_tolerance()
# reset_nord_api()


# idd=4017

# update_conf_nord_api(idd)

print("Loading module pure : para OK ! [ "+pure_count_left_api() + " ]")
# data_id,data_cnf_names,data_used=get_random_api()
# print(data_id,data_cnf_names,data_used)


# get_active_goo()