import pyautogui
from PIL import Image
import tempfile

# TODO решить проблему с отловом клика в любой области (pynput не робит почему-то)
# TODO очень много левых библиотек при установке. Попытаться поискать иные варианты

import tkinter as tk

class App:
   def __init__(self):
       root = tk.Tk()
       red_label = tk.Label(root, text="RED: ")
       red_label.place(x=10, y=10)
       red_entry = tk.Entry(root)
       red_entry.place(x=100, y=10)

       green_label = tk.Label(root, text="GREEN: ")
       green_label.place(x=10, y=60)
       green_entry = tk.Entry(root)
       green_entry.place(x=100, y=60)

       blue_label = tk.Label(root, text="BLUE: ")
       blue_label.place(x=10, y=110)
       blue_entry = tk.Entry(root)
       blue_entry.place(x=100, y=110)



       submit = tk.Button(root, text="Submit",
                          fg="red",
                          command=lambda: get_color_by_value(red_entry.get(), green_entry.get(), blue_entry.get(), root))

       submit.place(x=200, y=150)


       root.geometry("500x300")
       self.root = root
   def run(self):

       self.root.mainloop()

def get_color_by_value(r,g,b, root):
   """setting color block to GUI according to entries values"""
   # TODO вставить проверку на числа
   result = Image.new(size=(50, 50), color=(r, g, b), mode='RGB')


def get_color_from_cursor(x, y):
   """returning the result color tuple and picture with this color in dict"""
   t = tempfile.NamedTemporaryFile()
   screenshot = pyautogui.screenshot(t.name)
   color = screenshot.getpixel((x, y))
   result = Image.new(size=(50, 50), color=color, mode='RGBA')
   result.save('result.png')
   t.close()
   return {'color': color, 'color_picture': result}


if __name__ == '__main__':
   a = App()
   a.run()

