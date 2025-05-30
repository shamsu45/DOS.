from scapy.all import sniff, UDP

def packet_callback(packet):
    if UDP in packet:
        print(f"Packet captured: {packet.summary()}")

def start_sniffing(interface=None):
    print("Starting packet sniffing...")
    # Sniff UDP packets
    sniff(iface=interface, filter="udp", prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (or leave blank for default): ").strip()
    start_sniffing(interface)￼Enter
