import scapy.all as scapy #import library for us to craft and send packets
import optparse as op #importing the  optparse library to accept command line input from the user

ob_parse = op.OptionParser() #creating a blank parse object/instance
ob_parse.add_option("-t", "--iprange", dest="ipentry", help="IP Range") #defining the command line argument
value, key = ob_parse.parse_args() #Storing parse values from input stream from command line
ipentry = value.ipentry #parsing the ip address from the command line stream

arp_request = scapy.ARP() #ARP packet object created and stored
#scapy.ls(scapy.ARP)
arp_request.pdst = ipentry #passing the ip address entered into the arp request
#print(arp_request.summary())

broadcast = scapy.Ether() #creating the ethernet frame for the broadcast
broadcast.dst = "ff:ff:ff:ff:ff:ff" #broadcast MAC addresss
#print(broadcast.summary())

arp_request_broadcast = broadcast/arp_request #combining the MAC address and the frame to create the request
#print(arp_request_broadcast.show())

scapy.srp(arp_request_broadcast) #sedning of the request created 
answered, unanswered = scapy.srp(arp_request_broadcast, timeout = 1) #caoturing the answered packets
#print(answered.summary())

for packet in answered:
    print("Response#: %s | IP:%s | MAC:%s" %(answered.index(packet)+1,packet[1].psrc, packet[1].hwsrc))

print("Packets have been answered")