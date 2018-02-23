import socket
import threading

class Server:
  def __init__(self, family = socket.AF_INET, sockType = socket.SOCK_STREAM):
    self.__sock = socket.socket(family, sockType)
    self.__server_address = ('localhost', 10000)
    self.__clienses = []
    print('starting up on %s port %s' % self.__server_address)

  def SeparetaConnection(self, connection, client_address, name):
    try:
      
      while True:
        print("waiting for the message...")
        recvmsg = connection.recv(1024).decode("utf-8")
        if recvmsg == "exit":
          print("%s closed the session" % name)
          break
        print('received message from %s: %s' % (name,recvmsg))
        for i in self.__clienses:
          if name != i[0]:
            msg = i[0] + ": " + recvmsg
            i[1].sendall(msg.encode())
      return True
    except (socket.error, v):
      print("Error - %s", v)
      return False
    finally:
      for i in self.__clienses:
        if name == i[0]:
          self.__clienses.remove(i)
      connection.close()
  
  def Run(self):
    self.__sock.bind(self.__server_address)
    self.__sock.listen(5)
    print('waiting for client connections')
    while True:
      connection, client_address = self.__sock.accept()
      name = connection.recv(1024).decode("utf-8")
      self.__clienses.append((name, connection))
      print('connection from', name)
      proc = threading.Thread(target=self.SeparetaConnection, args=(connection, client_address, name))
      proc.start()
    

  
  

