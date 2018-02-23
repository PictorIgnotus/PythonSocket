import server
from multiprocessing import pool

if __name__ == '__main__':
  mainServer = server.Server()

  mainServer.Run()