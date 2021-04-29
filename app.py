from tkinter import *
from tkinter import ttk

app = Tk()

units = []

with open("unit.txt", "r") as f:
    units = [item.strip() for item in f.readlines()]


app.minsize(485, 300)
app.title("Unit Converter")


#### First Variable ####

# Adding Label
ttk.Label(app, text="First Input Field\n").grid(column=0, row=1)

# Adding Entries
first_var = StringVar()
first_field = ttk.Entry(app, textvariable=first_var,
                        width=20).grid(column=0, row=3)

# Adding unit Combo box

first_box = StringVar()
first_box_field = ttk.Combobox(
    app, textvariable=first_box, width=5)
first_box_field.grid(column=1, row=3)
first_box_field['values'] = units
first_box_field.current(0)


#### Second Variable ####

# Adding Label
ttk.Label(app, text="Second Input Field\n").grid(column=3, row=1)

# Adding Entries
second_var = StringVar()
first_field = ttk.Entry(app, textvariable=second_var,
                        width=20).grid(column=3, row=3)


# Output Field
ttk.Label(app, text="Result", width=0).grid(column=2, row=4)
output_var = StringVar()
output_field = ttk.Entry(app, state="readonly", textvariable=output_var, width=20).grid(
    column=2, row=5)

# Adding unit Combo box

second_box = StringVar()
second_box_field = ttk.Combobox(
    app, textvariable=second_box, width=5)
second_box_field.grid(column=4, row=3)
second_box_field['values'] = units
second_box_field.current(0)


# Label "TO"
ttk.Label(app, text="to").grid(column=2, row=2)

# Buttons

exit_btn = ttk.Button(app, text="exit").grid(column=1, row=7)
convert_btn = ttk.Button(app, text="Convert").grid(column=2, row=7)

app.mainloop()
