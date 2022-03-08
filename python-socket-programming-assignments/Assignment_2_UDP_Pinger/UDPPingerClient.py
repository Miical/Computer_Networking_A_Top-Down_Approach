from socket import *
from time import sleep, time

ServerAddress = ('127.0.0.1', 12000)

for i in range(1, 11):
  startTime = time()
  message = f"Ping {i} {startTime}"
  clientSocket = socket(AF_INET, SOCK_DGRAM)

  try:
    clientSocket.settimeout(1.0)
    clientSocket.sendto(message.encode(), ServerAddress)
    rec_message, address = clientSocket.recvfrom(1024)
  except timeout:
    print('Request timed out')
    clientSocket.close() 
  else:
    print(rec_message.decode(), ', RTT =', time() - startTime, 's')