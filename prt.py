from tkinter import *
window=Tk()

window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_intrest():
    principle = int(principle_entry.get())
    rate = int(rate_entry.get())
    time = int(time_entry.get())
    i = (principle*rate*time)/100
    intrest = round(i,2)
    name = username.get()

    result_label.destroy()

    output_message=Label(result_frame,text=name+", your intrest is "+str(intrest),bg="lightcyan",font=("Calibri",12),width=42)
    output_message.place(x= 20 , y = 40)
    output_message.pack()

app_label=Label(window, text="Intrest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principle_label=Label(window, text="Enter principle", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principle_label.place(x = 20 , y = 135)
principle_entry = Entry(window,text = "",bd = 2 , width = 15)
principle_entry.place(x = 150 , y = 130)

rate_label=Label(window, text="Enter rate", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x = 20 , y = 165)
rate_entry = Entry(window,text = "",bd = 2 , width = 15)
rate_entry.place(x = 150 , y = 160)

time_label=Label(window, text="Enter time", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x = 20 , y = 195)
time_entry = Entry(window,text = "",bd = 2 , width = 15)
time_entry.place(x = 150 , y = 190)

calculate_button = Button(window,text = "CALCULATE" , fg = "black" , bg = "cyan" , bd = "4" , command = calculate_intrest)
calculate_button.place(x = 20 , y = 250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
