import os
from os import system,path
import re
from speak import speak
import parser
from prompt_user import prompt


def directory(inp):
    inp = parser.parse(inp)

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
            speak(f"{dir_name} already exist")
            choice = prompt("Do you still want to create a new directory","Still want to create a directory? ","Enter your choice")
            choice = choice.lower()
            possible_choice = ["yes","yea","okey","okay","ok","affirmative","yup","yep","roger","very well","sure","totally"]
            if choice in possible_choice:
                    dir_name = prompt("Enter the name of the directory","Enter the name of the directory","Please enter the name")

                    system(f"mkdir /home/raviteja/{dir_name}")

                    speak(f"{dir_name} has been created")


        else:
            system(f"mkdir /home/raviteja/{dir_name}")

            speak(f"{dir_name} is created")
