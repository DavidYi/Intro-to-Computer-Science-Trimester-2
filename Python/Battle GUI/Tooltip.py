import tkinter

class Tooltip(object):
    # Creates a tooptip box for a widget.
    def __init__(self, widget, text):
        self.tipwindow = None
        self.text = text
        self.widget = widget
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        
    def enter(self, event):        
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox( "insert" )
        x += self.widget.winfo_rootx() + 27
        y += self.widget.winfo_rooty() + 27
        
        # Creates a toplevel window
        self.tipwindow = tw = tkinter.Toplevel( self.widget )
        
        # Leaves only the label and removes the app window
        tw.wm_overrideredirect( 1 )
        tw.wm_geometry( "+%d+%d" % ( x, y ) )
        label = tkinter.Label( tw, text = self.text, justify = tkinter.LEFT,
                   background = "#ffffe0", relief = tkinter.SOLID, borderwidth = 1,
                   font = ( "tahoma", "8", "normal" ) )
        label.pack( ipadx = 1 )
    
    def close(self, event):
        self.close_window()
            
    def close_window (self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()