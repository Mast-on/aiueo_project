import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Entry Test')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='Username', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

label2 = ttk.Label(frame1, text='Password', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

# Username Entry
username = StringVar()
username_entry = ttk.Entry(
    frame1,
    textvariable=username,
    width=20)
username_entry.grid(row=0, column=1)

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=0, sticky=W)

button1 = ttk.Button(
    frame2, text='OK',
    command=lambda: print("%s," % (username.get())))
button1.pack(side=LEFT)

button2 = ttk.Button(frame2, text='Cancel', command=quit)
button2.pack(side=LEFT)

def addChar(text):
    return lambda: username_entry.insert(tk.END, text)

frame_dan = {}

for row_dan in range(5):
    frame_dan[row_dan] = ttk.Frame(frame1, padding=(0, 5))
    frame_dan[row_dan].grid(row=row_dan+3, column=1, sticky=W)

moji = [
    ['あ','い','う','え','お'],
    ['か','き','く','け','こ'],
    ['さ','し','す','せ','そ'],
    ['た','ち','つ','て','と'],
    ['な','に','ぬ','ね','の'],
    ['は','ひ','ふ','へ','ほ'],
    ['ま','み','む','め','も'],
    ['や','','ゆ','','よ'],
    ['ら','り','る','れ','ろ'],
    ['わ','を','ん','゛','゜'],
    ['ゃ','ゅ','ょ','っ','ー']
    ]

for i in range(11):
    for j in range(5):
        button = ttk.Button(
            frame_dan[j], text=moji[i][j],
            command= addChar(moji[i][j])
        )
        button.pack(side=RIGHT)


def leftKey(event):
    print ("Left key pressed")

def rightKey(event):
    print ("Right key pressed")
        
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)

root.mainloop()