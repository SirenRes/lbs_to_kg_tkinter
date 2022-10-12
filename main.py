import tkinter.ttk
import tkinter


window = tkinter.Tk()
window.title("Lbs to Kg Converter")
window.minsize(width=220, height=100)
window.maxsize(width=220, height=100)
window.config(padx=25, pady=25)

#input
input = tkinter.ttk.Entry(width=10)
input.insert(tkinter.END, string="0")
input.grid(row=0, column=1)

#button
def button_click_event():
    label3["text"] = int(int(input.get()) * 0.45359237)
button = tkinter.ttk.Button(text="Calculate", command=button_click_event)
button.grid(row=2, column=1)

#labels
label1 = tkinter.ttk.Label(text="Lbs", font=("Arial", 10, "bold"))
label1.grid(row=0, column=2)
label2 = tkinter.ttk.Label(text="is equal to", font=("Arial", 10, "bold"))
label2.grid(row=1, column=0)
label3 = tkinter.ttk.Label(text="0", font=("Arial", 10, "bold"))
label3.grid(row=1, column=1)
label4 = tkinter.ttk.Label(text="Kg", font=("Arial", 10, "bold"))
label4.grid(row=1, column=2)


window.mainloop()
