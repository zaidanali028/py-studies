from scapy.all import ARP, Ether, srp

# Define the target IP range (e.g., local network range)
target_ip = "192.168.1.1/24"  # Adjust this to your local network range

# Create an ARP request packet to ask "who has" for each IP in the range
arp_request = ARP(pdst=target_ip)
ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

# Stack the ARP request on top of the Ethernet frame
packet = ether_frame/arp_request

# Send the packet and receive the response
result = srp(packet, timeout=3, verbose=False)[0]

# Process the result and display the list of live devices
live_devices = []
for sent, received in result:
    live_devices.append(received.psrc)

print("Live devices on the network:")
for device in live_devices:
    print(f" - {device}")
