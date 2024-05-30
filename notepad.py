from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #save file as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate('<<Cut>>')


def copy():
    TextArea.event_generate('<<Copy>>')


def paste():
    TextArea.event_generate('<<Paste>>')


def about():
    messagebox.showinfo('About', 'This project is Developed By Ganesh Deshmukh')
    # messagebox.askokcancel('okCancel', "Are you sure")


if __name__ == '__main__':
    # basic notepad setup
    root = Tk()
    root.title('Untitled - Notepad')
    root.geometry("644x788")

    # Add TextArea
    TextArea = Text(root, font="Inter 16", selectbackground="black")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # lets create a menubar
    MenuBar = Menu(root)


    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To Open new file
    FileMenu.add_command(label="New", command=newFile, font="Inter 14")

    # To open already existing file
    FileMenu.add_command(label="Open", command=openFile, font="Inter 14")

    # To save the Current File
    FileMenu.add_command(label="Save", command=saveFile, font="Inter 14")
    # adding a seperator
    FileMenu.add_separator()
    # to quit app
    FileMenu.add_command(label="Exit", command=quitApp, font="Inter 14")
    # FileMenu.configure(font="Inter 14") instead of writing configuration on each option we can use configure option
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut, font="Inter 14")
    EditMenu.add_command(label="Copy", command=copy, font="Inter 14")
    EditMenu.add_command(label="Paste", command=paste, font="Inter 14")
    MenuBar.add_cascade(label="Edit", menu=EditMenu, )  # adding to MenuBar
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about, font="Inter 14")
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends

    root.config(menu=MenuBar)

    # Adding Scrollbar using rules
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
