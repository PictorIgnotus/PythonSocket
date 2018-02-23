import socket, time, initializecliens


class Cliens:
  def __init__(self, name, family = socket.AF_INET, typeOfSock = socket.SOCK_STREAM):
    self.sock = socket.socket(family, typeOfSock)
    self.initializeCliens = initializecliens.InitializeCliens(name)

  def SendName(self):
    self.sock.sendall(self.initializeCliens.GetName().encode())

  def ConnectToServer(self, server_address):
    print('connecting to %s port %s' % server_address)
    try:
      self.sock.connect(server_address)
      self.SendName()
      self.initializeCliens.ChangeConnected(True)
    except socket.error:
      print('ERROR')
      self.initializeCliens.ChangeConnected(False)

  def SendMessage(self, message): 
    print('cliens sending the message: %s' % message)
    self.sock.sendall(message.encode())
    print("Message sent")

  def DisConnectServer(self):
    print("Disconnect")
    self.sock.sendall("exit".encode())
    self.sock.close()
    self.initializeCliens.ChangeConnected(False)

  def IsConnected(self):
    return self.initializeCliens.IsConnected()

