import tkinter
import tkinter.scrolledtext

root = tkinter.Tk(screenName="Chat")

button_connect = tkinter.Button(root, text="Connect")
button_connect.pack()

label_connect = tkinter.Label(root, text="Information about connection")
label_connect.pack()

mainFrame = tkinter.Frame(root,width=300, height=10)
mainFrame.pack()

textArea = tkinter.scrolledtext.ScrolledText(mainFrame, height=3) #tkinter.ScrolledText.ScrolledText(root, wodth=300, height=80)
textArea.pack()
textArea.

button_1 = tkinter.Button(root, text="My name")
button_1.pack()

root.mainloop()