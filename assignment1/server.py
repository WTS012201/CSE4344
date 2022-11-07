# Name: William Sigala
# ID: 1001730022

import socket
import threading
import os
import sys
import signal
import json

### Default settings
DATA_LEN = 1024
FORMAT = 'utf-8'
DEFAULT = (socket.gethostbyname(socket.gethostname()), 8080)

### Establishing Host:Port connection
HOST = sys.argv[1] if len(sys.argv) == 3 else DEFAULT[0]
PORT = int(sys.argv[2]) if len(sys.argv) == 3 else DEFAULT[1]
ADDR = (HOST, PORT)

### Function for handling a client
def client_handler(conn, addr):
    ### Receive request
    req = conn.recv(DATA_LEN).decode(FORMAT)
    
    ### Parse out information from request and store in dictionary
    headers = {}
    for d in req.split('\r\n')[:-2]:    # parse http req
        headers[d[0:d.find(' ')]] = d[d.find(' ') + 1:]

    ### Display connection info
    print(f"Connection params: {conn}")
    print(f"Client request:\n{json.dumps(headers, indent=4, sort_keys=True)}")


    ### Format the filepath requested for reading
    file = headers["GET"].split()[0]
    if file.startswith("//pages/"):
        path = "." + file[1:]
    elif file.startswith("/pages/"):
        path = "." + file
    else:
        path = './pages/' + file

    ### If file exists read file data and send it back to client
    ### If file doesn't exist send back 404 Not Found
    if os.path.exists(path):
        with open(path, 'r') as f:
            body = f.read()
            conn.send(f"HTTP/1.1 200 OK\r\n\r\n{body}".encode(FORMAT))
    else:   conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode(FORMAT))
    conn.close()
    print()

if __name__ == "__main__":
    ### Open server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    signal.signal(signal.SIGINT, lambda u, v: sys.exit(server.close()))

    ### Bind server address to socket
    try:    server.bind(ADDR)
    except OSError as e:
        print(f"OSError: {e}")
        sys.exit()

    ### Start the server
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}\n")

    ### Accept a client connection and handle it in a separate thread
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")