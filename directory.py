from os import system,path
import re
from tkinter import *
from speak import speak


def prompt(to_speak,label_text,prompt):

    name = ""
    count = 0
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
        #global count
        name = var.get()
        if not input:
            speak(prompt)
        else:
            count = 1
            main.destroy()

    button = Button(main,text = "Proceed",fg = "white",bg = "#1287A8",command =  get_input)
    button.grid()
    speak(to_speak)
    if name:
        return name
    main.mainloop()



def directory(inp):

    def load_file():
        with open("directory.db","r") as file:
            for line in file:
                yield(line.strip("\n"))

    lines = load_file()
    dir_name = ""

    for line in lines:

        try:
            search_pattern = re.compile(rf"{line}\,(\w+)",re.IGNORECASE)
            res = search_pattern.search(inp)
            dir_name = res.group(1)

            break

        except:
            if inp == line:

                dir_name = prompt("Enter the name of the  directory","Enter the name of the directory","Please enter the name of the directory")

                break


    if not dir_name:
        speak("I didn't understand")
    else:
        if path.isdir(f"/home/raviteja/{dir_name}"):
            choice = prompt("Directory {dir_name} already exist","Do you want to change into that directory","Please enter your choice")

            if choice.lower() == "yes" or choice.lower() == "change":
                system(f"cd /home/raviteja/{dir_name}")
            elif choice.lower() == "no":
                choice = prompt("Do you still want to create a new directory","Want to create a directory? ","Enter your choice")
                if choice.lower() == "yes":
                    dir_name = prompt("Enter the name of the directory","Enter the name of the directory","Please enter the name")

                    system(f"mkdir /home/raviteja/{dir_name}")

                    speak("{dir_name} has been created")

                    usr_choice = prompt(f'Do you want change into the "{dir_name}" directory',f'Do you want change into the "{dir_name}" directory',"Yes or No")

                    if usr_choice.lower() == "yes" or usr_choice.lower() == "change":
                        system(f"cd /home/raviteja/{dir_name}")
        else:
            system(f"mkdir /home/raviteja/{dir_name}")

            speak("{dir_name} is created")

            usr_choice = prompt(f'Do you want change into the "{dir_name}" directory',f'Do you want change into the "{dir_name}" directory',"Yes or No")

            if usr_choice.lower() == "yes" or usr_choice.lower() == "change":
                system(f"cd /home/raviteja/{dir_name}")
