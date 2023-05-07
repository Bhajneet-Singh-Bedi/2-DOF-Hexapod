# This will be the GUI app for 2-DOF hexapod.

# Goal is to create an app which contains: two controls for movement.
#   1. Make left, right controller -> Which will specify to move to that that side (yawing to that side). LEFT    RIGHT
#   2. Make vertical slider controller, which will specify the speed and tell it to move forward or backward.



import tkinter as tk
from tkinter import ttk
from PIL import Image

def main():
    root = tk.Tk()
    root.title('Hexapod Bot')
    root.resizable(False,False)
    root.geometry("350x250")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    img=Image.open('D://Study Material//College//Sem 6//Project//app//button_2.png')
    # width, height=img.size
    # print(str(width) + " " + str(height))
    # img = img.resize((200,226), Image.LANCZOS)


    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    btn_left= tk.PhotoImage(file='D://Study Material//College//Sem 6//Project//app//button_left.png')
    #lbl = ttk.Label(img=click_btn)
    ttk.Button(frm, image=btn_left, command=root.destroy).grid(column=1, row=0, pady=20)

    btn_right= tk.PhotoImage(file='D://Study Material//College//Sem 6//Project//app//button_right.png')
    #lbl = ttk.Label(img=click_btn)
    ttk.Button(frm, image=btn_right, command=root.destroy).grid(column=2, row=0, padx=10)

    vertical = tk.Scale(root, from_=-50, to=50, length=200).grid(column=3, row=0, padx=10, pady=15)
    #vertical.pack()
    root.mainloop()


if __name__ == "__main__":
    main()