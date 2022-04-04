from socket import *
import sys
if len(sys.argv) <= 1:
  print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
  sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('', 2333))
tcpSerSock.listen(20)
# Fill in end.
while 1:
  # Strat receiving data from the client
  print('Ready to serve...')
  tcpCliSock, addr = tcpSerSock.accept()
  print('Received a connection from:', addr)
  message = tcpCliSock.recv(2048).decode() # Fill in start. # Fill in end.
  print(message)
  # Extract the filename from the given message
  print(message.split()[1])
  filename = message.split()[1].partition("/")[2]
  print(filename)
  fileExist = "false"
  filetouse = "/" + filename
  print(filetouse)

  try:
    # Check wether the file exist in the cache
    f = open(filetouse[1:], "r") 
    outputdata = f.readlines() 
    fileExist = "true"
    # ProxyServer finds a cache hit and generates a response message
    tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
    tcpCliSock.send("Content-Type:text/html\r\n".encode())
    # Fill in start.
    for i in range(0, len(outputdata)): 
      tcpCliSock.send(outputdata[i].encode())
    tcpCliSock.send("\r\n".encode())
    # Fill in end.
    print('Read from cache') 
    # Error handling for file not found in cache
  except IOError:
    if fileExist == "false": 
      # Create a socket on the proxyserver
      c = socket(AF_INET, SOCK_STREAM) # Fill in start. # Fill in end.
      hostn = filename.replace("www.","",1) 
      print(hostn) 
      try:
        # Connect to the socket to port 80
        # Fill in start.
        print("connecting to", hostn, "...")
        c.connect((hostn, 80))
        print("connected")
        # Fill in end.
        # Create a temporary file on this socket and ask port 80 for the file requested by the client

        # fileobj = c.makefile('wb', None)
        # fileobj.write(("GET "+ filetouse + " HTTP/1.1\n\n").encode())
        c.send(("GET " + "/ HTTP/1.1\n").encode())
        c.send(("host:" + filename + "\n\n").encode())
        print("GET / HTTP/1.1")
        print("host:" + filename + "\n")
        # Read the response into buffer
        # Fill in start.
        print('response:')
        response = c.recv(4096)
        print(response)
        # Fill in end.
        # Create a new file in the cache for the requested file. 
        # Also send the response in the buffer to client socket and the corresponding file in the cache
        tmpFile = open("./" + filename, "wb")
        # Fill in start.
        tmpFile.write(response)
        tmpFile.close()

        tcpCliSock.send(response)
        # Fill in end.
      except:
        print("Illegal request") 
    else:
      # HTTP response message for file not found
      # Fill in start.
      tcpCliSock.send('HTTP/1.1 404 Not Found\n\n'.encode())
      # Fill in end.
  # Close the client and the server sockets 
  tcpCliSock.close() 
# Fill in start.
tcpSerSock.close()
# Fill in end.