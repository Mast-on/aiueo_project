import tkinter

root = tkinter.Tk()
root.title('title')
root.geometry('400x300')
def key_h(event):
    root.event_generate('<Motion>', warp=True, x=event.x-50, y=event.y)
def key_j(event):
    root.event_generate('<Motion>', warp=True, x=event.x, y=event.y+50)
def key_k(event):
    root.event_generate('<Motion>', warp=True, x=event.x, y=event.y-50)
def key_l(event):
    root.event_generate('<Motion>', warp=True, x=event.x+50, y=event.y)
def motion(event):
    print('motion {}, {}'.format(event.x, event.y))
root.bind('<KeyPress-h>', key_h)
root.bind('<KeyPress-j>', key_j)
root.bind('<KeyPress-k>', key_k)
root.bind('<KeyPress-l>', key_l)
root.bind('<Motion>', motion)
"""
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val1.set(False)
Val2.set(True)
CheckBox1 = tkinter.Checkbutton(text=u"content1", variable=Val1)
CheckBox2 = tkinter.Checkbutton(text=u"content2", variable=Val2)
CheckBox1.pack()
CheckBox2.pack()
"""
root.mainloop()