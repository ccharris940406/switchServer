import socket
import sys

host = ''
port = 50400

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

exit = 0

while True:
	conn, addr = sock.accept()
	print("Connected by: ", addr)
	while True:
		data = conn.recv(1024)
		print(data)
		if not data: break
		if data == 'exit':
			exit = 1
		conn.sendall(data)
	if exit: break
conn.close()