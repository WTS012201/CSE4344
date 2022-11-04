#from pydoc import ispath
import socket
import threading
import os
import sys
import signal

DATA_LEN = 1024
FORMAT = 'utf-8'

HOST = socket.gethostbyname(socket.gethostname())
PORT = sys.argv[1] if len(sys.argv) == 2 else 8080
ADDR = (HOST, PORT)

def client_handler(conn, addr):
    req = conn.recv(DATA_LEN).decode(FORMAT)
    headers = {}
    for d in req.split('\n'):
        headers[d[0:d.find(' ')]] = d[d.find(' ') + 1:]
    #print(headers)
    # print("New Connection")
    # print(f"Socket info: {conn}")
    # print(f"Address info: {addr}")

    #print(conn.send("HTTP/1.1 200 OK".encode(FORMAT)))
    print('.' + headers["GET"].split()[0], os.path.exists('.' + headers["GET"].split()[0]))
    if os.path.exists('.' + headers["GET"].split()[0]):
        conn.send("HTTP/1.1 200 OK".encode(FORMAT))
    else:
        conn.send("HTTP/1.1 404 Not Found".encode(FORMAT))

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    signal.signal(signal.SIGINT, lambda u, v: sys.exit(server.close()))

    try:
        server.bind(ADDR)
    except OSError:
        server.close()
        sys.exit()

    server.listen()
    print(f"Server is listening on {HOST}")
    while True:
        pass
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")