import Tkinter

root = Tkinter.Tk(screenName="Chat window")

label_connect = Tkinter.Label(root, text="Information about connection")
label_connect.pack()
label_info = Tkinter.Label(root, text="The information")
label_info.pack()

connected = False

def Connection():
  global connected
  if connected:
    label_info.config(text="Successfully closed the connection")
    button_connect.config(text="Connect")
    message_area.config(state="normal")
    message_area.delete("1.0", "end")
    message_area.config(state="disabled")
    connected = False
  else:
    label_info.config(text="Successfull connection")
    button_connect.config(text="Unconnect")
    connected = True

button_connect = Tkinter.Button(root, text="Connect", command=Connection)
button_connect.pack()

scrollbarm = Tkinter.Scrollbar(root)
message_area = Tkinter.Text(root, width=80, height =20, wrap="word", yscrollcommand=scrollbarm.set, borderwidth=2, highlightthickness=1)
message_area.tag_config("n", background="yellow", foreground="red")
message_area.tag_config("a", foreground="blue")
message_area.config(state="disabled")
message_area.pack()


scrollbare = Tkinter.Scrollbar(root) 
edit_area = Tkinter.Text(root, width=80, height=2, wrap="word",
                   yscrollcommand=scrollbare.set,
                   borderwidth=0, highlightthickness=0)
edit_area.pack()

def GetText(event):
  content = edit_area.get("1.0", "end")
  content = content.strip()
  if connected and content != "":
    message_area.config(state="normal")
    message_area.insert("end","You: " + content + "\n")
    message_area.config(state="disabled")
    message_area.see("end")
    edit_area.delete("1.0", "end")


button_1 = Tkinter.Button(root, text="Send")
button_1.bind("<Button-1>", GetText)
button_1.pack() 

root.mainloop()
