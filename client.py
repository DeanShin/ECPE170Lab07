#!/usr/bin/env python3

# Simple network socket demo - CLIENT
#
# Set script as executable via: chmod +x client.py
# Run via:  ./client.py <IP> <PORT>
#
# To connect to a server on the same computer, <IP> could
# either be 127.0.0.1 or localhost (they have the same meaning)
import argparse
import socket
import sys


def main():
    if len(sys.argv) != 3:
        print("Error: Program needs <IP> and <PORT> arguments")
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument('ip', action="store", type=str)
    parser.add_argument('port', action="store", type=int)
    args = parser.parse_args(sys.argv)

    ip = args.ip
    port = args.port

    # Create TCP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: could not create socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Connecting to server at " + ip + " on port " + str(port))

    # Connect to server
    try:
        s.connect((ip, port))
    except socket.error as msg:
        print("Error: Could not open connection")
        print("Description: " + str(msg))
        sys.exit()

    print("Connection established")

    # Send message to server
    string_unicode = "Tiger Roar!"
    raw_bytes = bytes(string_unicode, 'ascii')

    try:
        # Send the string
        # Note: send() might not send all the bytes!
        # You should loop, or use sendall()
        bytes_sent = s.sendall(raw_bytes)
    except socket.error as msg:
        print("Error: send() failed")
        print("Description: " + str(msg))
        sys.exit()

    print("Sent %d bytes to server" % bytes_sent)

    # Close socket
    try:
        s.close()
    except socket.error as msg:
        print("Error: unable to close() socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Sockets closed, now exiting")


if __name__ == "__main__":
    sys.exit(main())
