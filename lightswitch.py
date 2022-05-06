#main file for GUI
from phue import Bridge 
import tkinter as tk

b = Bridge('10.0.0.61')

def main():
    w = tk.Tk()
    w.geometry = ("610x400")
    
    lights = b.lights

    def set_lights(bri):
        for l in lights:
            print(bri)
            l.on = True
            l.brightness=int(bri)
    var = tk.DoubleVar()    
    dimmer = tk.Scale(w, from_ = 0, to = 254, variable=var, sliderlength = 50, width = 50, length = 380,command=set_lights)
    dimmer.pack()
    w.mainloop()


if __name__ =="__main__":
 main()
