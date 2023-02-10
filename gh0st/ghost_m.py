import os , random

country_as=["AE","AL","AM","AR","AT","AU","BA","BD","BE","BG","BR","BS","BY","CA","CH","CL","CN","CO","CR","CY","CZ","DE","DK","DZ","EE","EG","ES","FI","FR","GB","GE","GL","GR","HK","HR","HU","ID","IE","IL","IM","IN","IR","IS","IT","JP","KE","KH","KR","KZ","LI","LK","LT","LU","LV","MA","MC","MD","ME","MK","MN","MO","MT","MX","MY","NG","NL","NO","NZ","PA","PH","PK","PL","PT","QA","RO","RS","RU","SA","SE","SG","SI","SK","TH","TR","TW","UA","US","VE","VN","ZA"]


def run_vpn_ghost():
	os.system("pkill openvpn")
	cco=random.choice(country_as)
	ct="sudo cyberghostvpn --openvpn --traffic --country-code "+cco+" --connect"
	print("COUNTRY  !"+cco)
	try:
		os.system(ct)
	except Exception as e:
		print(str(e))
