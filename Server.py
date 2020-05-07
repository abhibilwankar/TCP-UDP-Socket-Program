import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET for IPv4
#socket.SOCK_STREAM for TCP Connection

host = ''
# host = 'localhost'
# host = socket.gethostname()
# we can use 'localhost' or socket.gethostname()
port = 65432
s.bind((host, port))

s.listen()
socketclient, address = s.accept()

print("Got connection from", address)

msg = socketclient.recv(1024)
msg = msg.decode('utf-8')

print(msg)