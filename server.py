import socket
#script for creating a TCP server

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind((host, port))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print('recived connection from: ' % str(address))
    message = 'hi, you are hooked'
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()