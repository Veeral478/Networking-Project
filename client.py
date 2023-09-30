import argparse
import socket
import pathlib
import os
import sys


arguments = len(sys.argv)

if arguments != 3:
    print("Error: Wrong number of arguments")
    sys.exit(1)
    # wrong number of arguments were given (There needs to be exactly 2)
else:
    out_file_n = sys.argv[2]
    host_name = sys.argv[1]
    #we store the arguments given in the above variables

try:
    ip_server = socket.gethostbyname(host_name)
    #tries the socket server

except socket.gaierror:
    print("Can not convert hostname to ip address")
    sys.exit(1)
    #we can not change the hostname to an ip address we print an error

filepath = pathlib.Path("output_file") / out_file_n
#filepath for use later

try:
    outfile = open(filepath, "wb")
    #output file location

except FileNotFoundError:
    print("The file was unable to be found")
    sys.exit(1)
    #the path to the file was not found

port = 6969
#port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((ip_server, port))
    dataReceived = clientSocket.recv(80)

    if os.path.getsize(filepath) >= 81:
        print("Exceeded file character limit of 80")
        clientSocket.close()
        outfile.close()
        sys.exit(1)
        #checks if the file contains more than 80 characters and gives an error if it is and closes the connection and file
    while dataReceived:
        outfile.write(dataReceived)
        dataReceived = clientSocket.recv(80)
#file transfer

clientSocket.close()
outfile.close()
#closes the connection and the file