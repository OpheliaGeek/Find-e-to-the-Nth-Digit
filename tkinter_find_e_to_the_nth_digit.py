"""
Programm to find e to Nth digit with GUI(Tkinter)
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
"""

from tkinter import Tk, END, StringVar, Entry, Button
from tkinter import ttk
from decimal import Decimal, getcontext
from math import factorial


def find_e(*args):
    """
    Function to get user input, generate and show e to the asked digit.
    If any errors appear - show information about it.
    *args needs for key <Return> binding
    """
    try:
        getcontext().prec = 1001
        num_e = 0
        for k in range(1000):
            num_e += (1 / Decimal(factorial(k)))

        decim_places = int(nth_digit.get())
        if 0 < decim_places <= 1000:
            result_e.set(str(num_e)[:(decim_places + 2)])
            label_result["foreground"] = "black"
            entrymain.delete(0, END)
        else:
            result_e.set(
                "Error. More than limit or non-negative integer numbers greater then 0")
            label_result["foreground"] = "red"
            entrymain.delete(0, END)
    except ValueError:
        result_e.set(
            "Error. Please use non-negative integer numbers greater then 0")
        label_result["foreground"] = "red"
        entrymain.delete(0, END)


# set main window
root = Tk()
root.title("Find e to nth digit")
root.configure(bg="#D5D8DC")
root.geometry("600x300")

# Task information
labelmain = ttk.Label(root, width=80, borderwidth=3,
                      relief="solid", background="#D4E6F1")
labelmain.configure(text="""
            \rGet result of Euler's number up to that many decimal places. Limit is 1000.
            \rPlease enter a non-negative integer number greater then 0""")
labelmain.grid(row=0, column=0, columnspan=2, padx=5, pady=3, sticky="nswe")

# Entry widget for user input
nth_digit = StringVar()
entrymain = Entry(root, width=80, borderwidth=3, textvariable=nth_digit)
entrymain.grid(row=1, column=0, padx=5, pady=3, sticky="nswe")

# Label widget to show result
result_e = StringVar()
label_result = ttk.Label(root, textvariable=result_e, wraplength=550,
                         borderwidth=3, relief="solid", background="#D4E6F1")
label_result.grid(row=2, column=0, columnspan=2, padx=5,
                  pady=3, sticky="nswe")

# Button widget to get information from Entry, pass it to function and get result
buttonmain = Button(root, text="Generate",
                    command=find_e, width=10, )
buttonmain.grid(row=1, column=1, padx=5, pady=3, sticky="nswe")

# allows to press key <Return>
root.focus()
root.bind("<Return>", find_e)

root.mainloop()
