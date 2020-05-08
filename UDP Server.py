import socket

host = '127.0.0.1'
port = 20001
buffersize = 1024

msgfromserver = 'Hello UDP Client'
bytesTosend = str.encode(msgfromserver)

# creating a datagram socket
udpserversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Binding 'HOST' & 'PORT'
udpserversocket.bind((host, port))
print('UDP Server is UP and Listening')

# Listen for incoming datagrams
while (True):
    bytesaddresspair = udpserversocket.recvfrom(buffersize)
    message = bytesaddresspair[0]
    address = bytesaddresspair[1]
    clientMsg = 'Message from Client: {}'.format(message)
    clientIP = 'Client IP Address: {}'.format(address)

    print(clientMsg)
    print(clientIP)

#     Sending a reply to client:
    udpserversocket.sendto(bytesTosend, address)
