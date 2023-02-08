import os

def run_vpn_ghost():
	try:
		os.system("sudo cyberghostvpn --openvpn --traffic --country-code SE --connect --connection TCP")
	except Exception as e:
		print(str(e))
