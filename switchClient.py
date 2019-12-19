import socket
import sys

host = '10.0.0.1'
port = 50400

msg = 'airSwitch'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
sock.sendall(msg)
data = sock.recv(1024)
print (data)
sock.close()