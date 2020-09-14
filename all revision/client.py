import socket
s=socket.socket()
s.connect(('localhost',4000))
content=""

content=input("enter the text:")
s.send(content.encode())
msg=s.recv(2000)
while msg:
    print(msg.decode())
    msg=s.recv(1024)
s.close()