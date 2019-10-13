#
#
#
#

#Importacion de librerias

from tkinter import *
import tkinter.scrolledtext as tkst
import tkinter as tk
import random

#variables globales
matriz = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

matrizM = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
letras=[]



#Definición de Funciones


def cargarBD():
    global letras
    try:
        archivoVL = open("ValorLetras.txt","r")
        linea=archivoVL.readline()

        while linea!="":
            letras.append(linea.split(sep=","))
            linea=archivoVL.readline()
        archivoVL.close
        
        return 
    except:
        return "Ocurrió un error"


def crearTablero():
    global matriz
    for i in range(0,15):
        for j in range(len(matriz[0])):
            casilla = Button(frame,width=2,height=1,bg="#9ba89f")
            casilla.grid(row=i+2, column=j+2)

    

def cargarBD():
    global letras
    try:
        archivoVL = open("ValorLetras.txt","r")
        linea=archivoVL.readline()

        while linea!="":
            letras.append(linea.split(sep=","))
            linea=archivoVL.readline()
        archivoVL.close
        
        return 
    except:
        return "Ocurrió un error"


def crearCasillasBonus():
    global matrizM
    listMulLetra = []
    listMulPalabra = []
    mulPalabra=random.randint(2,6)
    for i in range(0,10): # Hay 10 multiplicadores de letra
        filaL=random.randint(0,14)
        columnaL=random.randint(0,14)
        listMulLetra.append([filaL,columnaL])
        matrizM[filaL][columnaL] = 1
    while mulPalabra != 0:
        filaP=random.randint(0,14)
        columnaP=random.randint(0,14)
        listMulPalabra.append([filaP,columnaP])
        if matriz[filaP][columnaP]== 0:
            matriz[filaP][columnaP]=2
        mulPalabra-=1
    
def darLetras():
    global letras
    texto =Text(ventana,width = 3,height = 25)
    texto.place(x=420,y=70)
    for i in letras:
        texto.insert(tk.INSERT,i[0]+"="+i[1])
    texto.config(state= "disabled")


#Programa Principal
        
#Ventana
ventana = Tk()
ventana.title("PalabraCraft")
ventana.geometry("700x550")
ventana.config(bg="#cfc27c")
cargarBD()
#Frames
frame=Frame(ventana,bg="#cfc27c")
frame.place(x=40,y=80)

#Botones
crearTablero()

#Labels
darLetras()
crearCasillasBonus()
ventana.mainloop()
