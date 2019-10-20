#Creado por Natalia Vargas Reyes y Javier Rivera Madrigal

#Fecha de creación: 11/10/2019 5:00 pm

#Fecha de última modificación: 12/10/2019 11:00 pm

#Verión 3.7.2



#Importacion de librerias



from tkinter import *

from tkinter import font

from tkinter import messagebox

import tkinter.scrolledtext as tkst

import tkinter as tk

import random





#variables globales


matriz=[]

matrizBotones=[] #

listMulPalabra=[]

listMulLetra=[]

dicValoresLetras={} #

letras=[]

archivo = []

fichasJ1 = []

fichasJ2 = []


turno = True

proceso=0

 
#Definición de Funciones

def crearMatriz():

    '''

    Función:  Crea una matriz 15x15.

    Entradas: Ninguna.

    Salidas: Llama a cargarBD().

    '''

    for i in range(0,15):

        matriz.append([])

        for j in range(0,15):

            matriz[i].append(0)

            

    return cargarBD()



def cargarBD():

    '''

    Función: Llena una lista con las letras disponibles, valor y cantidad de las mismas.

    Entradas: Ninguna.

    Salidas: Llama a la funcion darFichas()

    '''

    

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



def darFichas():

    '''

    Función: Crea dos listas con las 7 fichas iniciales para cada jugador.

    Entradas: Ninguna.

    Salidas: Llama a la funcion darLetras().

    '''



    for i in archivo:

        letras.append(i[0])

    for i in range(0,7):

        letra = letras[random.randint(0,len(letras)-1)]

        fichasJ1.append(letra)

    for i in range(0,7):

        letra = letras[random.randint(0,len(letras)-1)]

        fichasJ2.append(letra)

    print(fichasJ1)

    print(fichasJ2)

    return darLetras()



def darLetras():

    '''

    Función: Coloca en la interfaz una lista con las letras y la cantidad de ellas.

    Entradas: Ninguna.

    Salidas: Llama a crearTablero.

    '''

   
    texto =Text(ventana,width = 3,height = 25)

    texto.place(x=420,y=70)

    for i in archivo:

        texto.insert(tk.INSERT,i[0]+"="+i[1])  #Inserta la letra y la cantidad en el TEXT.

    

    texto.config(state= "disabled") # Se utiliza para que no se pueda escribir en el TEXT.



    return crearTablero()

    

def crearTablero():

    '''

    Función: Crea el tablero con botones.

    Entradas: Ninguna.

    Salidas: la funcion colocarFichasJugador()

    '''

   

    for i in range(len(matriz)):

        for j in range(len(matriz)):
             
            casilla = Button(frameTablero,width=2,height=1,bg="#157d15",text="")
            casilla.grid(row=i, column=j)
            casilla.bind('<Button-1>',lambda e,i=i,j=j,casilla=casilla: colocarFichasJugador(i,j,casilla))
         
            
            
             
            
    return colocarFichasJugador()
             


    #Se deshabilitan ya que primero se selecciona la ficha que se quiere poner y luego

    #se selecciona la casilla

def colocarFichaTablero(i,j,casilla,ficha,fichas):
    try:
        if casilla["text"] == "":
            if ficha!=0:
                matriz[i][j] = ficha["text"]

                casilla.config(text=ficha["text"],bg = "#fff1c7")

                ficha.config(text="")
                
                fichas.pop(i)
                
                
                
    except:
        return 
        


            

  
def colocarFichasJugador(i=0,j=0,casilla=""):

    '''

    Función: Coloca las fichas del jugador en el tablero. ???

    Entradas: Ninguna.

    Salidas: Llama a la funcion crearCasillasBonus().

    '''
    if casilla!="":
        casilla.config(bg="yellow")

    if turno == True:       #decide si colocar las fichas del jugador 1 o 2

        fichas = fichasJ1

    else:

        fichas = fichasJ2

    for i in range(len(fichas)):

        ficha = Button(frameFichas,width=3,height=1,bg="#fff1c7",text=fichas[i],font=fichasFont)
        
        ficha.grid(row=0, column=i) #Coloca las fichas del jugador en la interfaz

        ficha.bind('<Button-1>',lambda e,i=i,ficha=ficha: colocarFichaTablero(i,j,casilla,ficha,fichas)) 
        

    return crearCasillasBonus()







def crearCasillasBonus():

    '''

    Función: Utiliza el random para colocar las casillas multiplicadoras en una matriz.

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''



    mulPalabra=random.randint(2,6) #cantidad de multiplicadores de palabra



    for i in range(0,10): # Hay 10 multiplicadores de letra

        filaL=random.randint(0,14)

        columnaL=random.randint(0,14)

        listMulLetra.append([filaL,columnaL])

        matriz[filaL][columnaL] = 1



    for i in range(mulPalabra):  # se crea una cantidad de 2-6 mul de palabra

        filaP=random.randint(0,14)

        columnaP=random.randint(0,14)

        listMulPalabra.append([filaP,columnaP])

        if matriz[filaP][columnaP]== 0:

            matriz[filaP][columnaP]= 2



    

            

    return 



def tiempoTurno(contador=0,contador1=0):

    '''

    Función: Crear un cronometro para el tiempo de cada turno.

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''



    if contador == 60:

        contador=0

        contador1+=1

        

    if contador1 == 1:

        messagebox.showinfo(" ", "Fin de su turno.")

        return     #solo lo puse para parar el tiempo al minuto 1...

        

    lblTiempoTurno['text'] = "Tiempo de turno: "+str(contador1)+':'+str(contador)

    proceso=lblTiempoTurno.after(1000, tiempoTurno,(contador+1),(contador1))

            

    return 



def tiempoPartida(contador=0,contador1=0):

    '''

    Función: Crear un cronometro para el tiempo de cada partida.

    Entradas: contador y contador1 (enteros)inicializados en 0.

    Salidas: Ninguna.

    '''
    
    global proceso

    btnIniciar.config(state='disabled')  #se deshabilita una vez iniciada la partida

   

    if contador == 60:

        contador=0

        contador1+=1

        

    if contador1 == 10:

        messagebox.showinfo(" ", "Fin de la partida.")

        return     #solo lo puse para parar el tiempo al minuto 10...

        

    lblTiempoPartida['text'] = "Tiempo de partida: "+str(contador1)+':'+str(contador)

    proceso=lblTiempoPartida.after(1000, tiempoPartida,(contador+1),(contador1))

            

    return 



def terminarPartida():

    '''

    Función: Eventos que suceden cuando se presiona el boton de terminar la partida (btnTerminar).

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''

    global proceso

    lblTiempoPartida.after_cancel(proceso)

    btnIniciar.config(state='normal')

    lblTiempoPartida['text'] = "Tiempo de partida: "



    return

    

#-------------Programa Principal-------------#



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

btnIniciar = Button(ventana,font=miFont,text="   Iniciar Partida  ",command=lambda:tiempoPartida())

btnIniciar.place(x=550,y=30)

btnTerminar = Button(ventana,font=miFont,text="Terminar Partida",command=lambda:terminarPartida())

btnTerminar.place(x=550,y=80)

btnFinalizar = Button(ventana,font=miFont,text=" Finalizar Turno ")

btnFinalizar.place(x=550,y=130)

btnImprimir = Button(ventana,font=miFont,text=" Imprimir matriz ")

btnImprimir.place(x=550,y=180)

#Labels

lblLetrasD = Label(ventana,font=miFont,text="Letras Disponibles:",bg="#cfc27c")

lblLetrasD.place(x=40,y=470)

lblTitulo = Label(ventana,font=tituloFont,text="Scrabble",bg="#cfc27c")

lblTitulo.place(x=10,y=0)

lblTiempoPartida = Label(ventana,font=tituloFont,text='Tiempo de partida:',bg="#cfc27c")

lblTiempoPartida.place(x=160,y=0)

lblTiempoTurno = Label(ventana,font=tituloFont,text='Tiempo de turno:',bg="#cfc27c")

lblTiempoTurno.place(x=160,y=30)



crearMatriz()

ventana.mainloop()
