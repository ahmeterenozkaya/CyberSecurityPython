import socket 

ip = "127.0.0.1"

for port in range(1,100):
	try:		
		sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sckt.settimeout(2.0)
		sckt.connect((ip,port))
		response = sckt.recv(1024)

		print(str(port),": open : Banner :",response.decode())
	except socket.timeout as t:
		if(port==80):
			httpMessage = "GET / HTTP/1.0\r\n\r\n"
			sckt.send(httpMessage.encode())
			httpRccv = sckt.recv(1024)
		print(str(port), ": use different method")

	except Exception as e:
		#print(str(port),": closed : reason:",str(e))
		pass
	finally:
		sckt.close()