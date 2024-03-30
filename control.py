from tkinter import Tk, Label, PhotoImage, Button, Canvas
from PIL import Image

root = Tk()
root.title("Control de motor")
root.geometry("500x500")
root.resizable(False, False)
motor_pausa = PhotoImage(file="rueda-p.png")
motor_derecha = PhotoImage(file="rueda-d.png")
motor_izquierda = PhotoImage(file="rueda-i.png")

label_motor = Label(root, image=motor_pausa)
label_texto = Label(root, text="Motor en pausa", font=("Segoe UI Semibold", 20))

def izquierda():
    label_motor.config(image=motor_izquierda)
    label_texto.config(text="Motor girando a la izquierda")
    boton_izquierda.config(state="disabled")
    boton_derecha.config(state="normal")
    boton_pausa.config(state="normal")

def derecha():
    label_motor.config(image=motor_derecha)
    label_texto.config(text="Motor girando a la derecha")
    boton_izquierda.config(state="normal")
    boton_derecha.config(state="disabled")
    boton_pausa.config(state="normal")

def pausa():
    label_motor.config(image=motor_pausa)
    label_texto.config(text="Motor en pausa")
    boton_izquierda.config(state="normal")
    boton_derecha.config(state="normal")
    boton_pausa.config(state="disabled")
    
imagen_izquierda = PhotoImage(file="flecha-i.png")
imagen_derecha = PhotoImage(file="flecha-d.png")
imagen_pausa = PhotoImage(file="pausa.png")

boton_izquierda = Button(root, image=imagen_izquierda, width=100, height=100, command=izquierda)
boton_derecha = Button(root, image=imagen_derecha, width=100, height=100, command=derecha)
boton_pausa = Button(root, image=imagen_pausa, width=100, height=100, command=pausa)

label_texto.place(relx=0.5, y=20, anchor="center")
boton_izquierda.place(x=100, y=50)
boton_pausa.place(x=200, y=50)
boton_derecha.place(x=300, y=50)
label_motor.place(x=150, y=200)

root.mainloop()
