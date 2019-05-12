from tkinter import *
from speak import speak

name = ""
def prompt(to_speak,label_text,prompt):

    main = Toplevel()
    label = Label(main,text = label_text)
    label.grid()
    var = StringVar()
    entry = Entry(main)
    entry.focus()
    entry.grid()
    entry.config(textvariable = var)

    def get_input():
        global name
        name = var.get()
        print(name)
        if not name:
            speak(prompt)
        else:
            main.destroy()

    button = Button(main,text = "Proceed",fg = "white",bg = "#1287A8",command =  get_input)
    button.grid()
    speak(to_speak)
    main.wait_window(main)
    return name
