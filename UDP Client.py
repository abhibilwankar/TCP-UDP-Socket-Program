import socket

msgfromclient = 'Hello UDP Server'
bytestosend = str.encode(msgfromclient)

Server_Add_Port = ('127.0.0.1', 20001)
buffersize = 1024

# Creating a UDP Socket at Client Side:
udpclientsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Sending to server using created UDP Socket
udpclientsocket.sendto(bytestosend, Server_Add_Port)

msgfromserver = udpclientsocket.recvfrom(buffersize)

msg = 'Message from Server {}'.format(msgfromserver[0])
print(msg)