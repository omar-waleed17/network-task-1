import socket
import time


HOST = '127.0.0.1'  
PORT = 65432        

packet_number = 0

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.settimeout(2) 

    while True:
        try:
            
            client_socket.sendto(str(packet_number).encode(), (HOST, PORT))
            print(f"Requested packet {packet_number}.")

           
            data, _ = client_socket.recvfrom(1024)
            received_packet_number = int(data.decode())

            if received_packet_number == packet_number:
                print(f"Received packet {packet_number}.")
                packet_number += 1

        except socket.timeout:
           
            print(f"Packet {packet_number} lost, resending...")
        
        time.sleep(1)  
