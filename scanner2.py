import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = input("Enter IP address: ")
port = int(input("Enter port: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("port is open")
    else:
        print("port closed")

portScanner(port)