#
#
#
#

#Importacion de librerias

from tkinter import *
from tkinter import font 
import tkinter.scrolledtext as tkst
import tkinter as tk
import random

#variables globales
 

fichasJ1 = []

fichasJ2 = []

archivo = []

turno = True

#Definición de Funciones
def crearMatriz():
    '''
    Función:  Crea una matriz 15x15
    Entradas: Ninguna
    Salidas: la matriz
    '''
    matriz=[]
    for i in range(0,15):
        matriz.append([])
        for j in range(0,15):
            matriz[i].append(0)
            
    return  matriz

def cargarBD():
    '''
    Función: Carga la base de datos suministrada
    Entradas: Ninguna
    Salidas: la funcion darFichas()
    '''
    global archivo
    try:
        archivoVL = open("ValorLetras.txt","r")
        linea=archivoVL.readline()

        while linea!="":
            archivo.append(linea.split(sep=","))
            linea=archivoVL.readline()
        archivoVL.close
        
        return darFichas()
    except:
        return "Ocurrió un error"

def crearTablero():
    '''
    Función: Crea el tablero con botones
    Entradas: Ninguna
    Salidas: la funcion colocarFichasJugador()
    '''
    global matriz
    for i in range(0,15):
        for j in range(len(matriz[0])):
            casilla = Button(frameTablero,width=2,height=1,bg="#157d15",state="disabled")
            casilla.grid(row=i+2, column=j+2)
    #Se deshabilitan ya que primero se selecciona la ficha que se quiere poner y luego
    #se selecciona la casilla
    return colocarFichasJugador()

def crearCasillasBonus():
    '''
    Función: Utliza el random para colocar las casillas multiplicadoras en una matriz
    Entradas: Ninguna
    Salidas: La funcion crearCasillasBonus()
    '''
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
            
    return crearCasillasBonus()


def darLetras():
    '''
    Función: Coloca en la interfaz una lista con las letras y la cantidad de ellas
    Entradas: Ninguna
    Salidas: Ninguna
    '''
    global archivo
    texto =Text(ventana,width = 3,height = 25)
    texto.place(x=420,y=70)
    for i in archivo:
        texto.insert(tk.INSERT,i[0]+"="+i[1])  #Inserta la letra y la cantidad 
    
    texto.config(state= "disabled") # Se utiliza para que no se pueda escribir en el
    
def darFichas():
    '''
    Función: crea dos listas con las 7 fichas de los jugadores
    Entradas: Ninguna
    Salidas: La funcion crearTablero()
    '''
    global archivo
    global fichasJ1
    global fichasJ2
    letras=[]
    for i in archivo:
        letras.append(i[0])
    for i in range(0,7):
        letra = letras[random.randint(0,len(letras)-1)]
        fichasJ1.append(letra)
    for i in range(0,7):
        letra = letras[random.randint(0,len(letras)-1)]
        fichasJ2.append(letra)
    return crearTablero()

def colocarFichasJugador():
    '''
    Función: Coloca las fichas del jugador en el tablero
    Entradas: Ninguna
    Salidas: La funcion darLetras()
    '''
    global fichasJ1
    global fichasJ2
    global turno

    if turno == True:       #decide si colocar las fichas del jugador 1 o 2
        fichas = fichasJ1
    else:
        fichas = fichasJ2
    for i in range(len(fichas)):
        ficha = Button(frameFichas,width=3,height=1,bg="#fff1c7",text=fichas[i],font=fichasFont)
        ficha.grid(row=0, column=i) #Coloca las fichas del jugador en la interfaz
        
    return darLetras()
#Programa Principal
        
matriz = crearMatriz()  #Crea las matrices
matrizM = crearMatriz()

#Ventana
ventana = Tk()
ventana.title("PalabraCraft")
ventana.geometry("700x550")
ventana.config(bg="#cfc27c")
miFont = font.Font (family ='Californian FB', size = 13, weight = "bold")
fichasFont = font.Font(family ='Cambria', size = 12, weight = "bold")
tituloFont = font.Font(family ='Chiller', size = 20, weight = "bold")
 

#Frames
frameTablero = Frame(ventana,bg="#cfc27c")
frameTablero.place(x=40,y=80)
frameFichas = Frame(ventana,bg="#cfc27c")
frameFichas.place(x=40,y=500)

#Botones 
btnTerminar = Button(ventana,font=miFont,text="Terminar Partida")
btnTerminar.place(x=545,y=30)
btnFinalizar = Button(ventana,font=miFont,text="Finalizar Turno")
btnFinalizar.place(x=550,y=110)
btnImprimir = Button(ventana,font=miFont,text="Imprimir matriz")
btnImprimir.place(x=550,y=160)
#Labels
lblLetrasD = Label(ventana,font=miFont,text="Letras Disponibles:",bg="#cfc27c")
lblLetrasD.place(x=40,y=470)
lblTitulo = Label(ventana,font=tituloFont,text="Scrabble",bg="#cfc27c")
lblTitulo.place(x=10,y=0)


cargarBD()

ventana.mainloop()
