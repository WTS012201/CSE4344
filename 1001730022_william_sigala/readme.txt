Name: William Sigala
ID: 1001730022

As per submission guidelines

### Instructions:
- To run client:
    `python client.py` to run client program on default settings or
    `python client.py < server_IP address >< port_no >< requested_file_name >`
    Server_IP address: The IP address for Web server.
    port_no:  The port on which the server is listening.
    requested_file_name: The name of the requested file.

    The requested file must be contained in the pages directory.
    If running client with arguments, include all arguments.
    Ex: `python client.py 127.0.1.1 8080 test.txt`

- To run server:
    `python server.py` to run server program on default settings or
    `python server.py < server_IP address >< port_no >`
    Server_IP address: The IP address for Web server.
    port_no:  The port on which the server is listening.

    If running server with arguments, include all arguments.
    Ex: `python server.py 127.0.1.1 8080`
    
IDE: Code - OSS
Python libs: socket, sys, time, os, threading, signal, json