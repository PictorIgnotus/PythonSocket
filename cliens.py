import socket, time, initializecliens
import threading


class Cliens:
  def __init__(self, name, root = None, family = socket.AF_INET, typeOfSock = socket.SOCK_STREAM):
    self.sock = socket.socket(family, typeOfSock)
    self.initializeCliens = initializecliens.InitializeCliens(name)
    self.root = root
    self.__messages = ""

  def SendName(self):
    self.sock.sendall(self.initializeCliens.GetName().encode())

  def ConnectToServer(self, server_address):
    print('connecting to %s port %s' % server_address)
    try:
      self.sock.connect(server_address)
      self.SendName()
      self.initializeCliens.ChangeConnected(True)

      proc = threading.Thread(target=self.WaitForMessage)
      proc.start()
    except socket.error:
      print('ERROR')
      self.initializeCliens.ChangeConnected(False)

  def SendMessage(self, message): 
    print('cliens sending the message: %s' % message)
    self.sock.sendall(message.encode())
    print("Message sent")

  def WaitForMessage(self):
    while True:
      try:
        recvmsg = self.sock.recv(1014).decode("utf-8")
        self.__messages += (recvmsg + '\n')
        if self.root != None:
          self.root.event_generate("<<SentMessage>>", when="tail")
      except socket.error:
        break

  def GetMessages(self):
    msg = self.__messages
    self.__messages = ""
    return msg

  def DisConnectServer(self):
    print("Disconnect")
    self.sock.sendall("exit".encode())
    self.sock.close()
    self.initializeCliens.ChangeConnected(False)

  def IsConnected(self):
    return self.initializeCliens.IsConnected()

