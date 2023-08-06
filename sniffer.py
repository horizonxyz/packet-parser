from scapy.all import *
import packet_structs_functions, packet_structs

with open('packet_id_list.txt', 'r') as f:
    lines = f.readlines()

packet_id_table = {}
for line in lines:
    values = line.strip().split(',')
    hex_value = hex(int(values[0], 16))
    string_value = values[1]
    packet_id_table[hex_value] = string_value

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        if tcp_dport == 10016 or tcp_dport == 10001:
            print(f"Incoming packet from {ip_src}:{tcp_sport} to {ip_dst}:{tcp_dport}")
            #print(packet.summary())
        if tcp_sport == 10016 or tcp_sport == 10001:
            print(f"Outgoing packet from {ip_src}:{tcp_dport} to {ip_dst}:{tcp_sport}")
            #print(packet.summary())

        # print first two bytes of the packet
        packet_id = int.from_bytes(bytes(packet[TCP].payload)[:2], byteorder='little')
        
        if packet_id == 0:
            return
        
        print(f"Packet ID: {hex(packet_id)}")
        print(bytes(packet[TCP].payload))

        if hex(packet_id) not in packet_id_table:
            print(f"Unknown Packet ID: {hex(packet_id)}")
            return

        try:
            packet_class = getattr(packet_structs, packet_id_table[hex(packet_id)])()
            packet_function = getattr(packet_structs_functions, f"print_{packet_id_table[hex(packet_id)]}")
            data = getattr(packet_structs, packet_id_table[hex(packet_id)]).from_buffer_copy(bytes(packet[TCP].payload))
            packet_function(data)
            print(f"Packet Function: {packet_function}")
        except Exception as e:
            print(e)

        

#sniff(filter="tcp", timeout=5, prn=packet_callback)

sniff(filter="port 10016 or port 10001", prn=packet_callback)