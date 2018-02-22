import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False

name = input("Your name: ")
server_address = ('localhost', 10000)


def ConnectToServer():
  print('connecting to %s port %s' % server_address)
  try:
    sock.connect(server_address)
    SendName()
    return True
  except socket.error:
    print('ERROR')
    return False

def SendName():
  sock.sendall(name.encode())

def SendMessage():
  message = input("Message: ")
  print('cliens sending the message: %s' % message)
  sock.sendall(message.encode())
  print("Send message")

def  DisConnectServer():
  print("Disconnect")
  sock.sendall("exit".encode())
  sock.close()

def Choice(x):
  x = str(x)
  global connected
  if not connected and x == '1':
    connected = ConnectToServer()
  elif connected and x == '1':
    SendMessage()
  elif connected and x == '2':
    DisConnectServer()
    
def PrintMenu():
  if not connected:
    print("1 - Connect to server")
  else:
    print("1 - Send message")
    print("2 - disconnect server")
  print("0 - Close")

x = 1




while str(x) != '0':
  PrintMenu()
  x = input("Choice[1-3]: ")
  Choice(x)

print("Close socket")
try:
  sock.close()
  print("Succeed to close")
except socket.error:
  print("Failed to close")

