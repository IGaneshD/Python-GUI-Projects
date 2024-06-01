from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox


current_x = 0
current_y = 0
cursor_color = "black"


def clear_drawing():
    drawingCanvas.delete("all")


def choose_color():
    customCurosrColor = askcolor()
    id = colorBar.create_rectangle(290, 20, 320, 50, fill=customCurosrColor[1])
    colorBar.tag_bind(id, '<Button-1>', lambda x: set_cursorcolor(customCurosrColor[1]))


def set_cursorcolor(color):
    global cursor_color
    cursor_color = color

def pensize_changer():
    # creating pen size resizer
    global currentPenSize
    currentPenSize = DoubleVar()

    penSizeSlider = Scale(colorBar, from_=1, to=50, orient='horizontal', variable=currentPenSize, width=15, length=200,
                          background='white')
    penSizeSlider.place(x=175, y=60)

def color_palettes():
    x1 = 10
    y1 = 20
    x2 = 40
    y2 = 50

    colors = ['black', 'blue', 'red', 'green', 'yellow', 'white', 'brown']

    for color in colors:
        id = colorBar.create_rectangle(x1, y1, x2, y2, fill=color)
        colorBar.tag_bind(id, '<Button-1>', lambda x: set_cursorcolor(color))
        x1 += 40
        x2 += 40

    askcolorBtn = Button(colorBar, text="Choose\nColor", width=8, height=2, font="Inter 8 bold", command=choose_color)
    askcolorBtn.place(x=330, y=16)

    clearCanvasBtn = Button(colorBar, text="Clear", width=8, height=2, font="Inter 8 bold", command=clear_drawing)
    clearCanvasBtn.place(x=410, y=16)

def locatecursor(e):
    global current_x, current_y
    current_x, current_y = e.x, e.y


def drawline(e):
    global current_x, current_y, cursor_color
    drawingCanvas.create_line((current_x, current_y, e.x, e.y), fill=cursor_color, width=currentPenSize.get())
    current_x, current_y = e.x, e.y

def createdrawingcanvas():
    # Entire Drawing Canvas Starts
    # Creating Frame to give border
    drawingCanvasBorderFrame = Frame(root, background="#00A", bd=0)

    # actual drawing canvas starts
    global drawingCanvas
    drawingCanvas = Canvas(master=drawingCanvasBorderFrame, background="#fff", cursor="hand2")
    drawingCanvas.place(relx=.1, rely=.1, anchor=CENTER)
    drawingCanvas.pack(expand=True, fill="both", padx=1, pady=1)
    # actual drawing canvas ends

    drawingCanvasBorderFrame.pack(expand=True, fill="both", padx=25, pady=25)  # packing canvas border frame
    # Entire Drawing Canvas Ends

    # bind events to drawing Canvas
    drawingCanvas.bind('<Button-1>', locatecursor)
    drawingCanvas.bind('<B1-Motion>', drawline)


def quitWhiteBoard():
    root.destroy()


def change_background(bgcolor):
    drawingCanvas.config(background=bgcolor)


def about():
    messagebox.showinfo('About', 'This WhiteBoard is Created By\nGanesh Deshmukh')


def createmenubar():
    # Creating Menu Bar
    menuBar = Menu(root)

    # Exit the WhiteBoard
    menuBar.add_command(label='Exit', command=quitWhiteBoard)

    # Change the Background of Drawing Canvas
    canvasBackground = Menu(menuBar, tearoff=0)
    canvasBackground.add_command(label='black', command=lambda: change_background('black'))
    canvasBackground.add_command(label='white', command=lambda: change_background('white'))
    canvasBackground.add_command(label='green', command=lambda: change_background('#002d04'))
    menuBar.add_cascade(label='Background', menu=canvasBackground)

    # About the whiteboard
    menuBar.add_command(label='About', command=about)
    root.config(menu=menuBar)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x800")
    root.title("WhiteBoard")
    root.configure(bg="#f0f0f0")

    createmenubar()


    # Creating Color Bar
    colorBar = Canvas(root, bg="#ffffff", width=550, height=110)
    colorBar.pack(fill="y", pady=15)
    color_palettes()
    # Color Bar Ends


    createdrawingcanvas()

    pensize_changer()

    root.mainloop()