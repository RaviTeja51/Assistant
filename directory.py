from os import system,path
import re
from tkinter import *
from speak import speak
from prompt_user import prompt

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
            choice = prompt(f"Directory {dir_name} already exist",f"Do you want to change into {dir_name}","Please enter your choice")

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

            speak(f"{dir_name} is created")

            usr_choice = prompt(f'Do you want change into the "{dir_name}" directory',f'Do you want change into the "{dir_name}" directory',"Yes or No")

            if usr_choice.lower() == "yes" or usr_choice.lower() == "change":
                system(f"cd /home/raviteja/{dir_name}")
