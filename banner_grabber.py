#banner grabber
import socket

s = socket.socket()

def grabber(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print(s.recv(1024))

def main():
    ip = input("input the IP: ")
    port = str(input("enter the port: "))
    grabber(ip, int(port))

main()