import pyfiglet
import sys
import socket
from datetime import datetime
import time

decoration_banner = pyfiglet.figlet_format("PORT SCANNER")
print(decoration_banner)

target = input("Enter Your Target Website To Scan For Ports > ")

# Defining a target
if len(sys.argv) == 2:

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid ammount of Argument")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    # will scan ports between 1 to 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} Is Open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nOops You Have Entered CTRL+C")
    print("Exiting")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("Mission Failed")
    time.sleep(2)
    print("Some error occured please try again later!!")
