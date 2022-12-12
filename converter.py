from tkinter import *
import math

window=Tk() 


def from_kg():
    gram=float(kg_input_text.get())*1000
    gram_output.delete("1.0", END)
    gram_output.insert(END,gram) 
    
    pound=float(kg_input_text.get())*2.20462
    pound_output.delete("1.0", END)
    pound_output.insert(END,pound) 
    
    ounce=float(kg_input_text.get())*35.274
    ounce_output.delete("1.0", END)
    ounce_output.insert(END,ounce) 

kg_label=Label(window,text="KG",width=15)
kg_label.grid(row=0,column=0)


kg_input_text=StringVar()
kg_input=Entry(window,textvariable=kg_input_text,width=27)
kg_input.grid(row=0,column=1)


convert_button=Button(window,text="Convert",command=from_kg,width=20)
convert_button.grid(row=0,column=2)




gram_output=Text(window,height=1,width=20)
gram_output.grid(row=1,column=0)


pound_output=Text(window,height=1,width=20)
pound_output.grid(row=1,column=1)


ounce_output=Text(window,height=1,width=20)
ounce_output.grid(row=1,column=2)


window.mainloop()