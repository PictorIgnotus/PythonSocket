import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

print('starting up on %s port %s' % server_address)

sock.bind(server_address)

sock.listen(1)
try:
  print('waiting for a client connection')
  connection, client_address = sock.accept()

  name = connection.recv(1024).decode("utf-8")
  print('connection from', name)

  recvmsg = ""
  while recvmsg != "exit":
    print("waiting for the message...")
    recvmsg = connection.recv(1024).decode("utf-8")
    if recvmsg != "exit":
      print('received message from %s: %s' % (name,recvmsg))
    else:
      print("%s closed the session" % name)
except socket.error:
  print("Error")
finally:
  connection.close()