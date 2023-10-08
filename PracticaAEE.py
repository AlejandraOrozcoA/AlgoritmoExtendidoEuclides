from tkinter import *
from tkinter import messagebox

# Variables globales
a = 0
b = 0
modulo = 0

# Ejecucion 
def ejecutar():
    if getValores():
        if validarBeta(b):
            if primosRelativos(a, b):
                mcd, x, y = euclidesExtendido(a, b)

                # Mostrar resultados en un label
                label4 = Label(ventana, text="X: " + str(x))
                label4.config(font=("Arial", 12))
                label4.grid(column=0, row=4, padx=10, pady=10, sticky="w")

                label5 = Label(ventana, text="Y: " + str(y))
                label5.config(font=("Arial", 12))
                label5.grid(column=1, row=4, padx=10, pady=10, sticky="w")

                # Mostrar funcion de encriptacion y desencriptacion
                # Encriptacion
                # C = (a * P + b) mod n
                label6 = Label(ventana, text="Funcion de encriptacion:")
                label6.config(font=("Arial", 12))
                label6.grid(column=0, row=5, padx=10, pady=10, sticky="w")

                label7 = Label(ventana, text= "C =" + str(a) + "P + " + str(b) + " mod " + str(modulo))
                label7.config(font=("Arial", 12))
                label7.grid(column=1, row=5, padx=10, pady=10, sticky="w") 

                # Desencriptacion
                # a^-1 = x
                # b2 es el inverso aditivo de b
                b2 = modulo - b
                # P = x*(C + (-b)) mod n
                
                label8 = Label(ventana, text="Funcion de desencriptacion:")
                label8.config(font=("Arial", 12))
                label8.grid(column=0, row=6, padx=10, pady=10, sticky="w")

                label9 = Label(ventana, text="P =" + str(x) + "(C + (" + str(b2) + ")) mod " + str(modulo))
                label9.config(font=("Arial", 12))
                label9.grid(column=1, row=6, padx=10, pady=10, sticky="w")

            else:
                messagebox.showinfo("Error", "Alfa y Beta no son primos coprimos, prueba con otro valor")
        else:
            messagebox.showerror("Error", "Beta debe ser mayor que 0 y menor o igual que el modulo, prueba con otro valor")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios y deben ser numeros")
            


# Obtener los valores de los campos de texto
def getValores():
    global a, b, modulo
    # Valida que los campos no esten vacios
    if txt1.get() == "" or txt2.get() == "" or text3.get() == "":
        return False
    # Valida que los campos sean numeros
    if not txt1.get().isdigit() or not txt2.get().isdigit() or not text3.get().isdigit():
        return False
    
    a = int(txt1.get())
    b = int(txt2.get())
    modulo = int(text3.get())
    
    if a < b:   
        aux = a
        a = b
        b = aux       

    print(a, b, modulo)
    return True

# Validar beta > 0 y beta <= modulo
def validarBeta(b):
    global modulo
    if b > 0 and b <= modulo:
        return True
    else:
        return False
    
# Verificar que alfa y beta sean primos relativos (Algoritmo de Euclides)
def primosRelativos(a, b):
    global modulo

    while b > 0:
        r = a % b
        a = b
        b = r
    if a == 1:
        return True
    else:
        return False

# Algoritmo de Euclides Extendido mgcd(a, b) = ax + by 
def euclidesExtendido(a, b):
    global modulo
    x = 0
    y = 1
    u = 1
    v = 0

    while b != 0:
        q = a // b
        r = a % b
        m = x - u * q
        n = y - v * q
        a = b
        b = r
        x = u
        y = v
        u = m
        v = n
    mcd = a

    #Si el resultado de x es negativo se calcula el inverso aditivo
    if x < 0:
        x = x + modulo
    
    return mcd, x, y

# Creacion de la ventana
ventana = Tk()
ventana.title("Practica AE y AEE")
ventana.geometry("500x400")

# Labels y campos de la ventana 
label1 = Label(ventana, text="Ingrese el valor de alfa: ")
label1.config(font=("Arial", 12))
label1.grid(column=0, row=0, padx=10, pady=10, sticky="w")
txt1 = Entry(ventana, width=20)
txt1.grid(column=1, row=0, padx=10, pady=10)

label2 = Label(ventana, text="Ingrese el valor de beta: ")
label2.config(font=("Arial", 12))
label2.grid(column=0, row=1, padx=10, pady=10, sticky="w")
txt2 = Entry(ventana, width=20)
txt2.grid(column=1, row=1, padx=10, pady=10)

label3 = Label(ventana, text="Ingrese el valor del modulo: ")
label3.config(font=("Arial", 12))
label3.grid(column=0, row=2, padx=10, pady=10, sticky="w")
text3 = Entry(ventana, width=20)
text3.grid(column=1, row=2, padx=10, pady=10)

# Botones de la ventana
btn1 = Button(ventana, text="Algoritmo de Euclides", command= ejecutar)
btn1.config(font=("Arial", 12))
btn1.grid(column=1, row=3, padx=10, pady=10, sticky="W")

ventana.mainloop()
