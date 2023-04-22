import tkinter as tk
win = tk.Tk()

win.geometry("312x324")

win.resizable(0, 0)
win.title("GUI Calculator")

input_value = ""
display_text = tk.StringVar()

def click_button(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)

def clear_button():
    global input_value
    input_value = ""
    display_text.set("")

def equal_button():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""


input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="grey",highlightthickness=2)

input_frame.pack(side=tk.TOP)
ip_field= tk.Entry(input_frame, font=('calibri', 18, 'bold'), textvariable=display_text, width=50, bg="#eee", bd=0,
                       justify=tk.RIGHT)
ip_field.grid(row=0, column=0)

ip_field.pack(ipady=10)

btns_frame = tk.Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()
clear_btn = tk.Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, cursor="hand2",
                      command=lambda: clear_button()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

mod_btn = tk.Button(btns_frame, text="%", fg="black", width=10, height=3, bd=0, cursor="hand2",
                       command=lambda: click_button("%")).grid(row=0, column=2, padx=1, pady=1)

divide_btn = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, cursor="hand2",
                       command=lambda: click_button("/")).grid(row=0, column=3, padx=1, pady=1)



btn_7 = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, cursor="hand2",
                  command=lambda: click_button(7)).grid(row=1, column=0, padx=1, pady=1)

btn_8 = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, cursor="hand2",
                  command=lambda: click_button(8)).grid(row=1, column=1, padx=1, pady=1)

btn_9 = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, cursor="hand2",
                  command=lambda: click_button(9)).grid(row=1, column=2, padx=1, pady=1)

multiply_btn = tk.Button(btns_frame, text="X", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                         command=lambda: click_button("*")).grid(row=1, column=3, padx=1, pady=1)



btn_4 = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                  command=lambda: click_button(4)).grid(row=2, column=0, padx=1, pady=1)

btn_5 = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                  command=lambda: click_button(5)).grid(row=2, column=1, padx=1, pady=1)

btn_6 = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                  command=lambda: click_button(6)).grid(row=2, column=2, padx=1, pady=1)

minus_btn = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                      command=lambda: click_button("-")).grid(row=2, column=3, padx=1, pady=1)


btn_1 = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                  command=lambda: click_button(1)).grid(row=3, column=0, padx=1, pady=1)
btn_2 = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, cursor="hand2",
                  command=lambda: click_button(2)).grid(row=3, column=1, padx=1, pady=1)
btn_3 = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                  command=lambda: click_button(3)).grid(row=3, column=2, padx=1, pady=1)

plus_btn = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                     command=lambda: click_button("+")).grid(row=3, column=3, padx=1, pady=1)

btn_0 = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, cursor="hand2",
                  command=lambda: click_button(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point_btn = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0,  cursor="hand2",
                      command=lambda: click_button(".")).grid(row=4, column=2, padx=1, pady=1)

equals_btn = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, cursor="hand2",
                       command=lambda: equal_button()).grid(row=4, column=3, padx=1, pady=1)


win.mainloop()


import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Basic Calculator")

display = Text(root, height=1, width=25)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', 'C', '=', '/', '%']

row = 1
col = 0

def click(key):
    if key == '=':
        result = eval(display.get('1.0', END))
        display.delete('1.0', END)
        display.insert(END, result)
    elif key == 'C':
        display.delete('1.0', END)
    else:
        display.insert(END, key)

for button in buttons:
    cmd = lambda x=button: click(x)
    tk.Button(root, text=button, width=5, height=2, command=cmd).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
