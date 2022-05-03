from phue import Bridge
import time
import tkinter as tk

w = tk.Tk()
w.geometry("610x400")
f = tk.Frame(w)
f.pack()
w.title("test")
slider = tk.Scale(f,tickinterval=1,length = 254,width=50, sliderlength = 50, label = "penis length",background="light blue",troughcolor="light blue")
slider.set(128)
slider.grid(row=254,columns=1)
slider.pack()
b = Bridge('10.0.0.61')
lights = b.lights
b.set_light(1,'bri',0)
bright = slider.get()
for l in lights:
 l.brightness = bright
w.mainloop()

