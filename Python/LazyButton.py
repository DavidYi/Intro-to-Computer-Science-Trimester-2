import tkinter
root = tkinter.Tk()
root.title("Lazy Buttons")
root.geometry("200x85")
#Creates the root window, which is the window where everything is happening.
#We made the title, the size of the root window in pixels, and the window itself

frame = tkinter.Frame(root)
#Creates a frame, which is basically a base where you can place something in this case widgets, in the root window
#any time you create new widget, you need to pass the thing that will contain the widget to the constructor of the new object
#We pass root to the Frame constructor
frame.grid()
#All widgets has this. It is associated with the layout manager, which lets you arrange the widgets

button1 = tkinter.Button(frame, text = "I do nothing")
#Makes button
button1.grid()
#Makes sure the button is visible

button2 = tkinter.Button(frame)
button2.grid()
#Creates a second button, which is blank, in the frame
button2.configure(text = "Me too!")
#This can modify a widget after it is created. This can be used in any widget option

button3 = tkinter.Button(frame)
button3.grid()
#Makes a third button, which is blank, in the frame
button3["text"] = "Same here!"
#This is another way to access the button's text option through a dictionary like interface.

root.mainloop()
#Kick off other window's event loop