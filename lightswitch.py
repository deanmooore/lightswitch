#main file for GUI
from phue import Bridge 
import tkinter as tk

b = Bridge('10.0.0.61')

def main():
    w = tk.Tk()
    w.geometry = ("610x400")
 
    def set_lights():
        for l in b.lights:
            l.on = True
            l.brightness=dimmer.get()
    
    dimmer = tk.Scale(w, variable=254, sliderlength = 50, width = 50, length = 380,command=set_lights)
    dimmer.pack()
    w.mainloop()


if __name__ =="__main__":
 main()
