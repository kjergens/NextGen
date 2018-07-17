import socket
import ssl
import threading
from queue import Queue

q = Queue()


def open_port(port):
    """
    Try to open the port.
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                        ssl_version=ssl.PROTOCOL_SSLv23)

    try:
        s.connect(("pythonprogramming.net", port))
        print('\nport', port, 'is open!', end="\n")
        s.close()

    except Exception:
        print(port, end=" ")


def port_scan():
    """
    Get the next port number off the queue, process it, mark it done, go to next.
    :return:
    """
    while q:
        open_port(q.get())
        q.task_done()


# Add port numbers to the queue
for num in range(440, 900):
    q.put(num)

# Create threads and set them to work opening ports
for x in range(30):
    t = threading.Thread(target=port_scan)
    t.daemon = True  # End process when done
    t.start()

q.join()  # Block printing until all tasks done
print('\n\nDone')

b't\x00d\x03\x83\x01\x01\x00d\x00S\x00'