import tkinter
import cliens


class CliensGUI:
  def __init__(self):
    self.__server_address = ('localhost', 10000)
    self.name = ""
    self.connected = False
    self.root = tkinter.Tk(screenName="Chat window")
    self.label_name = tkinter.Label(self.root, text="To use the app enter your name:")
    self.text_name = tkinter.Text(self.root, width=20, height = 1)
    self.label_connect = tkinter.Label(self.root, text="Information about connection")
    self.label_info = tkinter.Label(self.root, text="The information")
    self.button_connect = tkinter.Button(self.root, text="Connect", command=self.Connection)
    self.scrollbarm = tkinter.Scrollbar(self.root)
    self.message_area = tkinter.Text(self.root, width=80, height =20, wrap="word", yscrollcommand=self.scrollbarm.set, borderwidth=2, highlightthickness=1)
    self.scrollbare = tkinter.Scrollbar(self.root) 
    self.edit_area = tkinter.Text(self.root, width=80, height=2, wrap="word", yscrollcommand=self.scrollbare.set, borderwidth=0, highlightthickness=0)
    self.button_send = tkinter.Button(self.root, text="Send")

  def StartCliens(self):
    self.cliens = cliens.Cliens(self.name, self.root)

  def SetProperties(self):
    self.label_name.place(relx=.5, rely=0.4, anchor="c")
    self.text_name.place(relx=.5, rely=.5, anchor="c")
    self.message_area.config(state="disabled")
    self.button_send.bind("<Button-1>", self.SendText)
    self.root.bind("<Return>", self.GetName)
    self.root.bind("<<SentMessage>>", self.GetMessage)
    self.root.protocol("WM_DELETE_WINDOW", self.OnClosing)

  def OnClosing(self):
    self.cliens.DisConnectServer()
    self.root.destroy()

  def Connection(self):
    if self.cliens.IsConnected():
      self.cliens.DisConnectServer()
      self.cliens = cliens.Cliens(self.name, self.root)
      self.label_info.config(text="Successfully closed the connection")
      self.button_connect.config(text="Connect")
      self.message_area.config(state="normal")
      self.message_area.delete("1.0", "end")
      self.message_area.config(state="disabled")
    else:
      self.cliens.ConnectToServer(self.__server_address)
      if self.cliens.IsConnected():
        self.label_info.config(text="Successfull connection")
        self.button_connect.config(text="Unconnect")
      else:
        self.label_info.config(text="Unsuccessfull connection")


  def SendText(self, event):
    content = self.edit_area.get("1.0", "end")
    content = content.strip()
    if self.cliens.IsConnected() and content != "":
      self.message_area.config(state="normal")
      self.message_area.insert("end","You: " + content + "\n")
      self.message_area.config(state="disabled")
      self.message_area.see("end")
      self.edit_area.delete("1.0", "end")
      self.cliens.SendMessage(content)

  def GetMessage(self, event):
    messages = self.cliens.GetMessages()
    messages = messages.strip()
    self.message_area.config(state="normal")
    self.message_area.insert("end", messages + "\n")
    self.message_area.config(state="disabled")

  def GetName(self, event):
    name = self.text_name.get("1.0", "end")
    name = name.strip()
    if name != "":
      self.name = name
      self.text_name.pack_forget()
      self.label_name.pack_forget()
      self.UnHideAll()
      self.root.geometry("700x500")
      self.root.unbind("<Return>")
      self.StartCliens()

  def UnHideAll(self):
    self.button_connect.pack()
    self.label_connect.pack()
    self.label_info.pack()
    self.message_area.pack()
    self.edit_area.pack()
    self.button_send.pack()


  def Start(self):
    self.root.geometry("300x300")
    self.label_name.pack()
    self.text_name.pack()
    self.SetProperties()
    self.root.mainloop()



MainApp = CliensGUI()

MainApp.Start()
























