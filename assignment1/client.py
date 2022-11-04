import socket
import time
import sys
import time

DATA_LEN = 1024
FORMAT = 'utf-8'
DEFAULT = (8080, socket.gethostbyname(socket.gethostname()), "test.txt")

HOST = sys.argv[2] if len(sys.argv) == 4 else DEFAULT[1]
PORT = sys.argv[1] if len(sys.argv) == 4 else DEFAULT[0]
FILE = sys.argv[3] if len(sys.argv) == 4 else DEFAULT[2]
ADDR = (HOST, PORT)

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_add = ()
    client.connect(ADDR)
    print('Client has been established')

    send_time = time.time()
    client.send(f"GET /{FILE} HTTP/1.1\r\n\r\n".encode(FORMAT))

    res = client.recv(DATA_LEN).decode(FORMAT)
    status = res[:res.find('\r\n\r\n')]

    print('Status:\t', status)
    if status == "HTTP/1.1 200 OK":
        body = res[res.find("\r\n\r\n"):]
        print(body)
    else:   exit(0)

    recv_time = time.time()
    RTT = recv_time - send_time
    print('RTT:\t', RTT)

    client.close()