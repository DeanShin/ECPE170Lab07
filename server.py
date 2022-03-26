#!/usr/bin/env python3

# Simple network socket demo - SERVER
#
# Set script as executable via: chmod +x server.py
# Run via: ./server.py <PORT>

import socket
import sys


def main():
    if len(sys.argv) != 2:
        print("Error: Program needs <PORT> argument")
        sys.exit()

    # Tip: You should use argparse - this method
    # is sloppy and inflexible
    port = int(sys.argv[1])

    # Create TCP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: could not create socket")
        print("Description: " + str(msg))
        sys.exit()

    # Bind to listening port
    try:
        host = ''  # Bind to all interfaces
        s.bind((host, port))
    except socket.error as msg:
        print("Error: unable to bind on port %d" % port)
        print("Description: " + str(msg))
        sys.exit()

    # Listen
    try:
        backlog = 10  # Number of incoming connections that can wait
        # to be accept()'ed before being turned away
        s.listen(backlog)
    except socket.error as msg:
        print("Error: unable to listen()")
        print("Description: " + str(msg))
        sys.exit()

    print("Listening socket bound to port %d" % port)

    # Accept an incoming request
    try:
        (client_s, client_addr) = s.accept()
        # If successful, we now have TWO sockets
        #  (1) The original listening socket, still active
        #  (2) The new socket connected to the client
    except socket.error as msg:
        print("Error: unable to accept()")
        print("Description: " + str(msg))
        sys.exit()

    print("Accepted incoming connection from client")
    print("Client IP, Port = %s" % str(client_addr))

    # Receive data
    try:
        buffer_size = 4096
        raw_bytes = client_s.recv(buffer_size)
    except socket.error as msg:
        print("Error: unable to recv()")
        print("Description: " + str(msg))
        sys.exit()

    string_unicode = raw_bytes.decode('ascii')
    print("Received %d bytes from client" % len(raw_bytes))
    print("Message contents: %s" % string_unicode)

    # Close both sockets
    try:
        client_s.close()
        s.close()
    except socket.error as msg:
        print("Error: unable to close() socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Sockets closed, now exiting")


if __name__ == "__main__":
    sys.exit(main())
