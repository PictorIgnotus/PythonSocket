class InitializeCliens:
  def __init__(self, name):
    self.__name = name
    self.__connected = False

  def GetName(self):
    return self.__name

  def ChangeConnected(self, isConnected):
    self.__connected = isConnected

  def IsConnected(self):
    return self.__connected