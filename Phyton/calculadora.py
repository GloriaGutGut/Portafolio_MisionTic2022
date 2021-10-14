#variables de control:
#entero = IntVar()  # Declara variable de tipo entera
#flotante = DoubleVar()  # Declara variable de tipo flotante
#cadena = StringVar()  # Declara variable de tipo cadena
#booleano = BooleanVar()  # Declara variable de tipo booleana

from tkinter import *

def operacion(operador):
    if operador == ' + ':
        result.set(float(num1.get()) + float(num2.get()))
    elif operador == ' - ':
        result.set(float(num1.get()) - float(num2.get()))
    elif operador == ' * ':
        result.set(float(num1.get()) * float(num2.get()))
    else:
        result.set(float(num1.get()) / float(num2.get()))

root = Tk()
root.title('Calculadora')

root.config(bd=20)
num0 = StringVar()
num1 = StringVar()
num2 = StringVar()
result = StringVar()

Label(root, text='Numero 1').pack()
Entry(root, textvariable=num1).pack()

Label(root, text='Numero 2').pack()
Entry(root, textvariable=num2).pack()

Label(root, text='Resultado').pack()
Entry(root, textvariable=result, state=DISABLED).pack()

marco=Frame(root)
marco.pack()

Button(marco, text=' + ', command=lambda: operacion(' + ')).pack(side=LEFT)
Button(marco, text=' - ', command=lambda: operacion(' - ')).pack(side=LEFT)
Button(marco, text=' * ', command=lambda: operacion(' * ')).pack(side=LEFT)
Button(marco, text=' / ', command=lambda: operacion(' / ')).pack(side=LEFT)

root.mainloop()
