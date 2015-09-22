# Echo server program
import socket
import struct

HOST = ''                 
PORT = 2404              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l_onoff=1          
l_linger = 0
s.setsockopt(socket.SOL_SOCKET,socket.SO_LINGER,struct.pack('ii', l_onoff, l_linger))
#s.settimeout(1)
s.bind((HOST, PORT))
s.listen(10)
print 'listening on port 2404'

while True:
	conn, addr = s.accept()
	conn.settimeout(0.5)
	print 'New connection from %s:%d' % (addr[0], addr[1])
	data=''
	try:
		data = conn.recv(1024)
	except Exception,e:
		print 'no data'	
	if data=='':
		print 'no data do nothing'
	else:
		#conn.close()		
		conn.sendall(data)		

