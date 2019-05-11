from tkinter import *
from speak import speak
def prompt(to_speak,label_text,prompt):

    name = ""
    main = Toplevel()
    label = Label(main,text = label_text)
    label.grid()
    var = StringVar()
    entry = Entry(main)
    entry.focus()
    entry.grid()
    entry.config(textvariable = var)

    def get_input():
        print("function call has occured")

        global name
        name = var.get()
        if not input:
            speak(prompt)
        else:
            main.destroy()

    button = Button(main,text = "Proceed",fg = "white",bg = "#1287A8",command =  get_input)
    button.grid()
    speak(to_speak)

    print("in here")
    @get_input
    if name:
        return name
    main.mainloop()
