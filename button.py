from tkinter import *

count = 0
def click():
    global count
    count+=1
    print( count)
    print("HI")

window=Tk()
photo=PhotoImage(file="lk.png")
button=Button(window, 
              text="click me!",
                bg="black", 
                fg="#00FF00",
                command=click,
                font=("comic sans", 20),
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound=BOTTOM
                )

button.pack()
window.mainloop()