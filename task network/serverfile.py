import socket
import random
import time

HOST = '127.0.0.1' 
PORT = 65432      
PACKET_LOSS_RATE = 0.3  

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"Server listening on {HOST}:{PORT}")
    
    packet_number = 0
    
    while True:
      
        data, addr = server_socket.recvfrom(1024)
        received_packet_number = int(data.decode())
        
        if random.random() > PACKET_LOSS_RATE:
            print(f"Received request for packet {received_packet_number}. Sending packet {received_packet_number}.")
            server_socket.sendto(str(received_packet_number).encode(), addr)
        else:
            print(f"Simulated loss for packet {received_packet_number}. Not sending.")
        
        time.sleep(1) 
