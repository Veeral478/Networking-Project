import argparse
import socket
import pathlib
import os
import sys


arguments = len(sys.argv)
#number of arguments

if arguments != 2:
    print("Error: Wrong number of arguments")
    sys.exit(1)
    #if the number of arguments is incorrect it will print an error
else:   
    inp_file_n = sys.argv[1]
    #if the number of arguments is as expected it will set the name to that argument

filePath = pathlib.Path("input_file") / inp_file_n
#file path

try:
    inpfile = open(filePath, "rb")
except FileNotFoundError:
    print("The input file was not found")
    sys.exit(1)
#checks if theres a file that exists in the specified location else it will error and exit

port = 6969
#port

if os.path.getsize(filePath) >= 81:
    print("Exceeded file character limit of 80")
    sys.exit(1)
    #makes sure the file has less than or equal to 80 characters

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind(("", port))
    serverSocket.listen(1)
    #listens for client connecting and binds

    print("Waiting for client to connect")
    #waiting

    loop = True
    #for infinite loop

    while loop:
        clientSocket, clientAddress = serverSocket.accept() #client to server accepting
        print("Client is connected")
        dataSend = inpfile.read(80)
        #gets the file
 
        while dataSend:
            clientSocket.send(dataSend)
            dataSend = inpfile.read(80)

        clientSocket.close()
        inpfile.seek(0)
        #closes 

        print(f"File sent")
        #prints file was sent