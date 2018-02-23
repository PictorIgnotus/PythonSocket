import cliensapp

class Main:
  def __init__(self):
    self.__cliensApp = cliensapp.CliensApp()
  
  def StartApp(self):
    self.__cliensApp.StartCliens()

    while True:
      self.__cliensApp.PrintMenu()
      choice = input("Your choice[1-3]: ")
      if not self.__cliensApp.Choose(choice):
        break

if __name__ == '__main__':
  main = Main()
  main.StartApp()