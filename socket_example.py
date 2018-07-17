import socket
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

#server = 'github.com'
server = "pythonprogramming.net"
port = 443
server_ip = socket.gethostbyname(server)

print(server_ip)

s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)


request = "GET / HTTP/1.1\r\nHost: "+server+"\r\nConnection: close\r\n\r\n"
s.connect((server, port))

# convert str to byte
s.sendall(request.encode())

# download buffer
while True:
    results = s.recv(4096)
    if not results:
        s.close()
        break
    print(results)
