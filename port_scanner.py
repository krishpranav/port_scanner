#!/usr/bin/env python3

import sys
import socket
from datetime import datetime

def banner():
    print("PORT SCANNER")

def portscanner():

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Please enter ip of the traget")

    print("*" * 50)
    print("Scanning target: " + target)
    print("Scanning started at: " + str(datetime.now()))

    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\nScanning Stoped!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved!")
        sys.exit()
    except socket.error:
        print("\nCheck internet connection")
        sys.exit()

if __name__ == "__main__":
    portscanner()