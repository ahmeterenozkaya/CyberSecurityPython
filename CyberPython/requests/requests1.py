import requests

url = 'http://127.0.0.1/DVWA/login.php'
#headers = {'user-agent': 'btk-akademi/1.1.1'}
data = {'username':'admin','password':'password','Login':'Login'}
try:
	r = requests.post(url, data=data, allow_redirects=True)
	print(r.status_code)
	print(r.text)
	#print(r.headers)
#	print(r.headers.get('Date'))
except Exception as e:
	print(e)
	pass
