# Name: William Sigala
# ID: 1001730022

import socket
import sys
import time

### Default settings
DATA_LEN = 1024
FORMAT = 'utf-8'
DEFAULT = (socket.gethostbyname(socket.gethostname()), 8080,"test.txt")
socket.setdefaulttimeout(10)

### Establishing Host:Port connection and req file
HOST = sys.argv[1] if len(sys.argv) == 4 else DEFAULT[0]
PORT = int(sys.argv[2]) if len(sys.argv) == 4 else DEFAULT[1]
FILE = sys.argv[3] if len(sys.argv) == 4 else DEFAULT[2]
ADDR = (HOST, PORT)

if __name__ == "__main__":
    ### Open socket and connect to server address
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_add = ()
    client.connect(ADDR)
    print('Client has been established')
    print(f'Connection params: {client}\n')

    ### Start RTT time and send request
    send_time = time.time()
    client.send(f"GET /{FILE} HTTP/1.1\r\n\r\n".encode(FORMAT))

    ### Receive response and parse out status
    res = client.recv(DATA_LEN).decode(FORMAT)
    status = res[:res.find('\r\n\r\n')]
    print('Status:\t', status)

    ### If status is good, then display body
    if status == "HTTP/1.1 200 OK":
        body = res[res.find("\r\n\r\n") + 4:]
        print("\n", body)

    ### Print RTT
    recv_time = time.time()
    RTT = recv_time - send_time
    print('\nRTT:\t', RTT)

    ### Close connection
    client.close()