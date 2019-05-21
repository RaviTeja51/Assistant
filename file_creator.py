import os
import re
from pathlib import Path
import parser
import prompt_user
from speak import speak

file_name = ""
dir_name = ""
file_path = ""

def create_the_file(file_path):
    Path(file_path).touch()
    if os.path.isfile(file_path):
        speak(f"File {file_name}has been successfully created")

def copy_file(file_path):
    with open("blue_print_file.c") as inp_file:
        with open(file_path,"w") as opt_file:
            for line in inp_file:
                opt_file.write(line)

def create_file(inp):
    global file_name
    global dir_name
    global file_path


    inp = parser.parse(inp)
    print(inp)

    def load_file(file_inp):
        with open(f"{file_inp}","r") as f:
            for line in f:
                yield(line.strip("\n"))

    def get_file_dir_name(file_inp):

        global file_name
        global dir_name

        lines = load_file(file_inp)
        for line in lines:
            try:
                usr_inp_pattern = re.compile(rf"{line}\,(\w+(\.\w+)|(\w+))",re.IGNORECASE)
                usr_inp_matched = usr_inp_pattern.search(inp)
                file_name = usr_inp_matched.group(1)
                dir_name = prompt_user.prompt("Which directory","Enter the name of the directroy","Please enter the directroy name")
                break

            except:
                if inp == line:
                    file_name = prompt_user.prompt("Enter the name of the file ","What is the name of the file","Please enter the name of the file")
                    dir_name = prompt_user.prompt("Which directory","Enter the name of the directroy","Please enter the directroy name")
                    break


    get_file_dir_name("parsed_inp_file.txt")
    usr_opt = ["home","home directory","main directory"]
    if  not dir_name:
        get_file_dir_name("parsed_c_file.txt")
        print(file_name)

        if ".c" not in file_name:
            file_name = file_name + ".c"
        print(file_name)



    if dir_name in usr_opt:
            file_path = f"/home/raviteja/{file_name}"
            create_the_file(file_path)
            if ".c" in file_name:
                copy_file(file_path)

    elif dir_name:
        file_path = f"/home/raviteja/{dir_name}/{file_name}"
        create_the_file(file_path)
        if ".c" in file_name:
            copy_file(file_path)
    else:
        speak("I did not understand")

    if file_path:
        choice = prompt_user.prompt(f"Do you want to open {file_name}",f"Do you want to open {file_name}","Please enter your choice")
        choice = choice.lower()
        possible_choice = ["open","yes","change","yea","okey","okay","ok","affirmative","yup","yep","roger","very well","sure","totally"]
        if choice in possible_choice:
            os.system(f"atom {file_path}")
