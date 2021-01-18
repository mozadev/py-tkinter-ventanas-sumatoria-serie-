import tkinter
from tkinter import messagebox


def calcular()
    n1 = txtnumero1.get()

    if len(n1) == 0
        messagebox.showinfo(message=Ingrese numero de elementos de la serie 12+34+78+1516... !!, title=Mensaje)
        txtnumero1.focus()

    else
        n1 = int(n1)
        s = 0
        for i in range(1, n1+1)
            operacion = (2  i - 1)  (2  i)
            s = s + operacion

        area.insert(1.0, nla suma de la serie es  {}.format(s))


ventana = tkinter.Tk()  # instancia del formulario
ventana.title(Ventana Principal)
ventana.geometry(600x500)
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='numero elementos de la serie 12+34+78+1516... !')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=200, y=70)

boton = tkinter.Button(ventana, text=Calcular, command=calcular)
boton.place(x=200, y=120)
area = tkinter.Text(ventana)
area.config(width=30, height=10)
area.place(x=100, y=150)

paises = tkinter.StringVar(ventana)
paises.set(--------------)
combo = tkinter.OptionMenu(ventana, paises, --------------, alumno1, alumno2, alumno3)
combo.place(x=100, y=400)
ventana.mainloop()  # ejecutando formulario
