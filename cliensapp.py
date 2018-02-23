import cliens

class CliensApp:
  def __init__(self):
    self.__server_address = ('localhost', 10000)
  
  def StartCliens(self):
    self.__name = input("Your name: ")
    self.__cliens = cliens.Cliens(self.__name)

  def PrintMenu(self):
    if not self.__cliens.IsConnected():
      print("1 - Connect to server")
    else:
      print("1 - Send message")
      print("2 - Read received messages")
      print("3 - disconnect server")
    print("0 - Close")

  def Choose(self, choice):
    choice = str(choice)
    if choice == '0':
      return False

    if not self.__cliens.IsConnected() and choice == '1':
      self.__cliens.ConnectToServer(self.__server_address)
    elif self.__cliens.IsConnected() and choice == '1':
      message = input("Message: ")
      self.__cliens.SendMessage(message)
    elif self.__cliens.IsConnected() and choice == '2':
      print(self.__cliens.GetMessages())
    elif self.__cliens.IsConnected() and choice == '3':
      self.__cliens.DisConnectServer()
    else:
      print("No appropriate option")

    return True
    
