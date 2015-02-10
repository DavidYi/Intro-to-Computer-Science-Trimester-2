import tkinter
from test.test_tcl import tkinter

root = tkinter.Tk()
root.title("Labeler")
root.geometry("200x50")
#Creates the root window, which is the window where everything is happening.
#We made the title, the size of the root window in pixels, and the window itself

frame = tkinter.Frame(root)
#Creates a frame, which is basically a base where you can place something in this case widgets, in the root window
#any time you create new widget, you need to pass the thing that will contain the widget to the constructor of the new object
#We pass root to the Frame constructor
frame.grid()
#All widgets has this. It is associated with the layout manager, which lets you arrange the widget

label = tkinter.Label(frame, text = "I'm a label!")
#makes a label in the frame

label.grid()
#Ensures the label will be visible

root.mainloop()
#Kick off the window's event loop