import os
import socket

_socket = socket.socket()
_socket.bind(('localhost',8000))
_socket.listen(1)

while True:
    connection, address = _socket.accept()
    data = connection.recv(1024)
    request = data.decode("utf-8")
    print(data)
    address = data.split(' ')[1]

    if address == "/index.html" or address == "/":
        if os.path.exists("./index.html"):
            file = open("index.html",'r')
            connection.send("""HTTP/1.1 200 OK\n"+
            "Content-type: text HTML\n\n""" + file.read())
            file.close()
    elif address == "/about/aboutme.html":
        if os.path.exists("./about/aboutme.html"):
            file = open("about/aboutme.html",'r')
            connection.send("""HTTP/1.1 200 OK\n"+"Content-type: text HTML\n\n""" + file.read())
            file.close()    
    connection.close()
_socket.close()
