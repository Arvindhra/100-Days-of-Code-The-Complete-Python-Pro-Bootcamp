from tkinter import *

def converter():
    input_value = float(input_text.get())
    output_value = input_value * 1.60934
    output_label.config(text=str(round(output_value,2)))

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

input_text = Entry(width=15,justify="center")
input_text.grid(row=0,column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1,column=0)

output_label = Label(text="0")
output_label.grid(row=1,column=1)

km_label = Label(text="Km")
km_label.grid(row=1,column=2)

calculate_button = Button(text="Calculate",command=converter)
calculate_button.grid(row=2,column=1)

















window.mainloop()