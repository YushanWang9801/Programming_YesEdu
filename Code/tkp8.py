import tkinter as tk

def factorise():
    factors = []

    n = int(entry.get())
    if n and n > 0:
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
    print(factors)
    return factors

def handle_exit():
    window.destroy()


window = tk.Tk()
window.geometry("400x300")
tk.Label(window, text="Enter a number to be factorized").place(x=0, y=0)
entry = tk.Entry(window)
entry.place(x=200, y=0)
factorBtn = tk.Button(window, text="Factorise", command=factorise).place(x=180, y= 50)
exitBtn   = tk.Button(window, text="Exit"     , command=handle_exit).place(x=250, y=100)


window.mainloop()