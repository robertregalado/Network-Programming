import socket

HOST = 'https://www.facebook.com/'
PORT = 80
BUFFSIZE = 4096
ADDRESS = (HOST, PORT)

if __name__ == '__main__':
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect(ADDRESS)
    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        if not data:
            break
        clientSock.send(data.encode('utf-8'))
        data = clientSock.recv(BUFFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
    clientSock.close()
        
 
