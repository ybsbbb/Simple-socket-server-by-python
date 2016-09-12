import socket

HOST='127.0.0.1'
PORT=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    data=input("Enter your input:(Enter 'bye' to exit)")
    s.sendall(data.encode())
    if data=='bye':
        break
    data=s.recv(1024)
    print(data.decode())
s.close()
