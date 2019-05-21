from tkinter import *
from file_creator import create_file
from directory import directory

main = Tk()
main.title("Garuda")
text = Text(main,width = 50,height = 4,bg = "#535353",fg = "white",font = ("Helvetica",15))
text.focus()


def get_input(event):
    inp = text.get("1.0","end-1c")
    print(inp)
    text.delete("1.0","end")
    text.mark_set("insert","{}.{}".format(1,1))

    if "directory"  in inp or "folder" in inp:
        directory(inp)
    elif "file" in inp:
        create_file(inp)


text.bind("<Return>",get_input)
Label(main,text = "Hi, I am Garuda",fg = "#1A0315",bg ="#328CC1",font=("Script", 16)).grid(row = 0,column = 0,sticky = "ews")
text.grid(row = 1,column = 0)

main.mainloop()
