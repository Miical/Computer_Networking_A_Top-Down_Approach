from email.errors import MessageDefect
from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.163.com"
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
print('#', heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
messageCommand = 'STARTTLS\r\n'
print('#', messageCommand)
clientSocket.send(messageCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket = ssl.wrap_socket(clientSocket)

email = (base64.b64encode(''.encode()) + ('\r\n').encode())
password = (base64.b64encode(''.encode()) + ('\r\n').encode())
clientSocket.send('AUTH LOGIN\r\n'.encode())
print('#', 'AUTH LOGIN')
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.send(email)
print('#', email)
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.send(password)
print('#', password)
recv = clientSocket.recv(1024).decode()
print(recv)

mailfromCommand = "MAIL FROM: <miical2002@163.com>\r\n"
print('#', mailfromCommand)
clientSocket.send(mailfromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response.
mailfromCommand = "RCPT TO: <879754743@qq.com>\r\n"
print('#', mailfromCommand)
clientSocket.send(mailfromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send DATA command and print server response.
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send message data.
messageData = "From: miical2002@163.com\r\n"
clientSocket.send(messageData.encode())
messageData = "To: 879754743@qq.com\r\n"
clientSocket.send(messageData.encode())
messageData = "Subject: Hello World.\r\n"
clientSocket.send(messageData.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)