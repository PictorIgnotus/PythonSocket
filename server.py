import socket

class Server:
  def __init__(self, family = socket.AF_INET, sockType = socket.SOCK_STREAM):
    self.__sock = socket.socket(family, sockType)
    self.__server_address = ('localhost', 10000)
    self.__clienses = []
    print('starting up on %s port %s' % self.__server_address)

  def Run(self):
    self.__sock.bind(self.__server_address)
    self.__sock.listen(5)
    try:
      print('waiting for a client connection')
      connection, client_address = self.__sock.accept()

      name = connection.recv(1024).decode("utf-8")
      print('connection from', name)
      self.__clienses.append(name)

      while True:
        print("waiting for the message...")
        recvmsg = connection.recv(1024).decode("utf-8")
        if recvmsg == "exit":
          print("%s closed the session" % name)
          break
        print('received message from %s: %s' % (name,recvmsg))
        
    except socket.error:
      print("Error")
    finally:
      connection.close()

