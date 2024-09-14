import nmap

scanner = nmap.PortScanner()

ip = "10.0.2.1"
scanner.scan(ip,'0-100','-sV')
#print(scanner.scaninfo())

print(ip,":",scanner[ip].state())
print("Protocols:",scanner[ip].all_protocols())


print(scanner[ip]['tcp'].keys())
#print(scanner[ip]['tcp'][21]) #ftp

for port in scanner[ip]['tcp'].keys():
#	print(scanner[ip]['tcp'][port])
	name = scanner[ip]['tcp'][port]['name']
	product = scanner[ip]['tcp'][port]['product']
	version = scanner[ip]['tcp'][port]['version']
	print(port,name,product,version)
