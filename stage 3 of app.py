from tkinter import *
from tkinter import ttk

app = Tk()

units = []

with open("unit.txt", "r") as f:
    units = [item.strip() for item in f.readlines()]



app.title("Unit Converter")
unit1=[]
unit2=[]

def convert(val, unit_in, unit_out):
    unit = {'m':1, 'km':1000, 'cm':0.01, "mm":0.001}
    return first_var*unit[first_box]/unit[second_box]

def select_input():
    global unit1
    unit1 = first_box.get()

def select_output():
    global unit2
    unit2 = second_box.get()

def converter():
    try:
        global unit1, unit2
        output_var.set(str(convert(float(first_filed.get()), unit1, unit2)))

    except:
            output_var.set("Error")


#### Variable ####
first_var = IntVar()
first_box = StringVar()
output_var = IntVar()
second_box = StringVar()

# Adding Label
ttk.Label(app, text="First unit").grid(column=0, row=1)

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
first_box_field['values'] = units
first_box_field.current(0)


second_box_field = ttk.Combobox(
    app, textvariable=second_box, width=5)
second_box_field.grid(column=3, row=3, padx=10, pady=10)
second_box_field['values'] = units
second_box_field.current(0)


# Buttons #

exit_btn = ttk.Button(app, text="Exit").grid(column=1, row=7, padx=10, pady=10)

convert_btn = ttk.Button(app, text="Convert", command=converter).grid(column=2, row=7, padx=10, pady=10)

convert_btn = ttk.Button(app, text="Reset").grid(column=3, row=7, padx=10, pady=10)

for i in range(3):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
