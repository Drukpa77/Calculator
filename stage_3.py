from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

app = tk.Tk()


units = {}

#### Variable ####
first_var = IntVar()
first_box = StringVar()
output_var = IntVar()
second_box = StringVar()


def open_file():
    with open("unit.txt", "r") as f:
        _units = [unit.strip() for unit in f.readlines()]
        for unit in _units:
            split_unit = unit.split(",")
            units[split_unit[0]] = split_unit[1]


def convert_to_meter(val, unit):
    if(unit == "m"):
        return val

    unit_val = [val for key, val in units.items() if key == unit][0]

    return float(unit_val) * val


def calculate_value(final_unit, num1):

    result = 0

    for key, value in units.items():
        if(key == final_unit):
            result = float(num1) / float(value)

    if(result < 1):
        return format(result, "f")
    return round(result)


def convert():
    # Get Units
    initial_unit = first_box.get()
    final_unit = second_box.get()

    # Get Values
    get_value = first_var.get()

    if(initial_unit == final_unit):
        return output_var.set(get_value)

    value = convert_to_meter(get_value, initial_unit)

    return output_var.set(calculate_value(final_unit, value))


def main():
    open_file()

    # Title
    app.title("Unit Converter")

    # Adding Label
    ttk.Label(app, text="First unit").grid(column=1, row=1)
    ttk.Label(app, text="Input").grid(column=0, row=2)
    ttk.Label(app, text="Second Unit").grid(column=3, row=1)
    ttk.Label(app, text="Result", width=0).grid(column=2, row=4)
    ttk.Label(app, text="to").grid(column=2, row=2)

    # Adding Entries
    first_field = ttk.Entry(app, textvariable=first_var,
                            width=10).grid(column=0, row=3)
    output_field = ttk.Entry(app, state="readonly", textvariable=output_var, width=20).grid(
        column=2, row=5)

    # Adding unit Combo box
    first_box_field = ttk.Combobox(
        app, textvariable=first_box, width=5)
    first_box_field.grid(column=1, row=3, padx=10, pady=10)
    first_box_field['value'] = [unit for unit, _ in units.items()]
    first_box_field.current(0)

    second_box_field = ttk.Combobox(
        app, textvariable=second_box, width=5)
    second_box_field.grid(column=3, row=3, padx=10, pady=10)
    second_box_field['value'] = [unit for unit, _ in units.items()]
    second_box_field.current(0)

    # Buttons #

    ttk.Button(app, text="Exit", command=lambda: app.destroy()).grid(
        column=1, row=7, padx=10, pady=10)
    ttk.Button(app, text="Convert", command=convert).grid(
        column=2, row=7, padx=10, pady=10)

    # Responsiveness
    for i in range(3):
        app.grid_rowconfigure(i, weight=1)
        app.grid_columnconfigure(i, weight=1)

    # Key Bindings
    app.bind("<Escape>", lambda x: app.destroy())

    app.mainloop()


if(__name__ == "__main__"):
    main()
