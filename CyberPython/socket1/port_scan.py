import socket 

ip = "127.0.0.1"

for port in range(1,256):
	try:
		sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sckt.connect((ip,port))
		print(str(port),": open")
	except Exception as e:
		print(str(port),": closed")
	finally:
		sckt.close()
		