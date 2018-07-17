import socket
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,                    ssl_version=ssl.PROTOCOL_SSLv23)

print(s)
server = 'pythonprogramming.net'


def port_scan(portno):
    try:
        s.connect((server, portno))
        s.close()
        return True
    except:
        return False


for x in range(400, 450):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                        ssl_version=ssl.PROTOCOL_SSLv23)

    if port_scan(x):
        print('Port', x, 'is open!!!')
    else:
        print('Port', x, 'is closed.')

