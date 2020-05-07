import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
host = ''
port = 65432
msg = 'Hello Client/Server'
s.connect((host, port))

s.send(bytes(msg))
s.send(msg.encode('utf-8'))

s.close()
