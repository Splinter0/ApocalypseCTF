from scapy.all import *

capture = rdpcap('test1.pcap')
ping_data = ""

for packet in capture:
	if packet[ICMP].type == 8: # Echo request
		ping_data += packet.load[16:32]
print(ping_data)
