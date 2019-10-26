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

import time



#variables globales

global matriz

global listMulPalabra

global listMulLetra

global letras

global archivo

global fichasJ1

global dichasJ2

global turno

global ponerNombre

global tiempoPartida

global tiempoTurno



matriz=[]

listMulPalabra=[]

listMulLetra=[]

letras=[]

archivo = []

fichasJ1 = []

fichasJ2 = []

tiempoPartida = ''

tiempoTurno = ''

turno = True

ponerNombre=True

proceso=0

proceso2=0



#Definición de Funciones

def ventanaInicial():

    '''

    Función:  Colocar objetos en el frame 1 y frame sobre la ventana.

    Entradas: Ninguna.

    Salidas: .

    '''

    

    frame1.grid(row=0,column=0, rowspan=30, columnspan=30, sticky=(E,W,N,S))

    

    lblImagen.place(x=170,y=420)



    lblnombreJuego.grid(row=5,column=10, rowspan=5, columnspan=9, sticky=(E,W,N,S))

    lblJugador1.grid(row=13,column=9, rowspan=1, columnspan=4, sticky=(N,S))

    lblJugador2.grid(row=15,column=9, rowspan=1, columnspan=4, sticky=(N,S))

    

    entJugador1.grid(row=13,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))

    entJugador2.grid(row=15,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))



    btnJugar.grid(row=18,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))



    frame2.grid_remove()





def onEnter(event):

    '''

    Función:  Abre la ventanaJuego al dar enter en el segundo entry.

    Entradas: El evento.

    Salidas: ventanaJuego()

    '''

    return ventanaJuego()



def ventanaJuego():

    '''

    Función:  Colocar objetos en el frame 2 y frame sobre la ventana.

    Entradas: Ninguna.

    Salidas: .

    '''



    eventoBotonJuego()

    crearMatriz()

    

    frame2.grid(row=0,column=0, rowspan=30, columnspan=30, sticky=(E,W,N,S))



    lblImagen2.place(x=850,y=540)

    

    frameTablero.place(x=100,y=180)

    frameFichas.place(x=100,y=610)





    btnIniciar.place(x=830,y=50)

    btnTerminar.place(x=830,y=120)

    btnComenzar.place(x=830,y=190)

    btnFinalizar.place(x=830,y=260)

    btnImprimir.place(x=830,y=330)





    lblLetrasD.place(x=100,y=580)

    

    lblTitulo.place(x=100,y=40)

    lblTiempoPartida.place(x=100,y=100)

    lblTiempoTurno.place(x=100,y=130)



    lblTurno.place(x=500,y=100)

    lblJugador.place(x=500,y=130)



    lblPuntaje.place(x=830,y=430)

    lblJugadorA.place(x=830,y=470)

    lblPuntajeA.place(x=1000,y=470)

    lblJugadorB.place(x=830,y=500)

    lblPuntajeB.place(x=1000,y=500)

    frame1.grid_remove()

    



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

        print(archivo)

        return darFichas()

    except:

        return "Ocurrió un error"



def darFichas():

    '''

    Función: Crea dos listas con las 7 letras iniciales para cada jugador.

    Entradas: Ninguna.

    Salidas: Llama a la funcion darLetras().

    '''



    for i in archivo:

        letras.append(i[0])

    for j in range(0,7):

        letra = letras[random.randint(0,len(letras)-1)]

        letra2 = letras[random.randint(0,len(letras)-1)]
        
        fichasJ1.append(letra)

        fichasJ2.append(letra2)

        for h in archivo:
            if letra in h:
                h[1]=int(h[1])-1
            if letra2 in h:
                h[1]=int(h[1])-1


    print(fichasJ1)

    print(fichasJ2)

    print(archivo)

    return darLetras()





def darLetras():

    '''

    Función: Coloca en la interfaz una lista con las letras y la cantidad de ellas.

    Entradas: Ninguna.

    Salidas: Llama a crearTablero.

    '''

    texto =Text(frame2,width = 3,height = 25)

    texto.place(x=500,y=170)

    #archivo contiene las letras con sus valores y cantidades

    for i in archivo:

        texto.insert(tk.INSERT,i[0]+"="+i[2][:1])  #Inserta la letra y la cantidad en el TEXT.

    

    texto.config(state= "disabled") # Se utiliza para que no se pueda escribir en el TEXT.



    return crearTablero()

    

def crearTablero():

    '''

    Función: Crea el tablero con botones.

    Entradas: Ninguna.

    Salidas: la funcion colocarFichasJugador()

    '''

   

    for i in range(0,15):

        for j in range(len(matriz[i])):

            casilla = Button(frameTablero,width=2,height=1,bg='#81BEF7',text="")

            casilla.grid(row=i, column=j)

            casilla.bind('<Button-1>',lambda e,i=i,j=j,casilla=casilla: colocarFichasJugador(i,j,casilla)) #Evento click derecho

  

            

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



    for l in matriz:

        print(l)



   

    #print(listMulPalabra)#Podemos ver una lista con coordenadas de los multiplicadores

    #print(listMulLetra)



            

    return colocarFichasJugador()





def colocarFichaTablero(i,j,casilla,ficha,fichas):

    pass

    '''

    Función: Coloca las fichas que el jugador seleccionó,en el tablero. 

    Entradas: i,j,casilla,ficha,fichas.

    Salidas: Ninguna.

    '''

    print(i,j)

    try:

        if casilla["text"] == "":

            if ficha["text"]!= "":

                #if matriz[i][j] != 0: #Si la casilla no es cero, es porque hay un valor que se debe multiplicar

                    #actualizarPuntaje()

                    

                matriz[i][j] = ficha["text"]

                for l in matriz:

                    print(l)

                casilla.config(text=ficha["text"],bg = "#fff1c7")

                fichas.remove(ficha["text"])

                print(fichas)

                ficha.destroy()

                return revisarBonus(i,j)

                

                           

    except Exception as e:
        print(e)
        return 

def revisarBonus():
    pass
    

def actualizarPuntaje():

    '''

    Función: Actualizar los puntajes.

    Entradas: .

    Salidas: .

    '''

    pass





def colocarFichasJugador(i,j,casilla):



    '''

    Función: Coloca las letras de los jugadores en las fichas. 

    Entradas: Ninguna.

    Salidas: Llama a la funcion crearCasillasBonus().

    '''

    if casilla["text"] == "":

        casilla.config(bg="#A70202")

        

    print(i,j)

    if turno == True:       #decide si colocar las fichas del jugador 1 o 2

        fichas = fichasJ1



    else:

        fichas = fichasJ2

    fila=len(fichas)
    colocar=0
    print(fichasJ1)
    while  fila!=0:
         
        ficha = Button(frameFichas,width=3,height=1,bg="#fff1c7",text=fichas[colocar],font=fichasFont)
        ficha.grid(row=0, column=colocar) #Coloca las fichas del jugador en la interfaz

        ficha.bind('<Button-1>',lambda e,i=i,ficha=ficha: colocarFichaTablero(i,j,casilla,ficha,fichas)) 
        
        fila-=1
        colocar+=1
    if colocar < 7:
        while colocar != 7:
              
            ficha = Button(frameFichas,width=3,height=1,bg="#fff1c7",font=fichasFont)
            ficha.grid(row=0, column=colocar) #Coloca las fichas del jugador en la interfaz
            colocar += 1



    return 





def tiempoTurno(contador=0,contador1=0):

    '''

    Función: Crear un cronometro para el tiempo de cada turno.

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''



    #NO SÉ QUÉ CON ESTO. IGNORAR DE MOMENTO

    nombres=eventoBotonJuego()

    jugador.set('Jugador: '+nombres[0])



    

    #---------------------------------------#

        

    btnComenzar.config(state='disabled')

    btnFinalizar.config(state='normal')

    btnTerminar.config(state='normal')

    global proceso2

    if contador == 60:

        contador=0

        contador1+=1

        

    if contador1 == 1:

        messagebox.showinfo(" ", "Fin de su turno.")

        return     #solo lo puse para parar el tiempo al minuto 1...

        

    lblTiempoTurno['text'] = "Tiempo de Turno: "+str(contador1)+':'+str(contador)

    proceso2=lblTiempoTurno.after(1000, tiempoTurno,(contador+1),(contador1))

            

    return 





def tiempoPartida(contador=0,contador1=0):

    '''

    Función: Crear un cronometro para el tiempo de cada partida.

    Entradas: contador y contador1 (enteros)inicializados en 0.

    Salidas: Ninguna.

    '''

    global proceso

    btnIniciar.config(state='disabled')  #se deshabilita una vez iniciada la partida

    btnComenzar.config(state='normal')



    if contador == 60:

        contador=0

        contador1+=1

        

    if contador1 == 10:

        messagebox.showinfo(" ", "Fin de la partida.")

        return    #solo lo puse para parar el tiempo al minuto 10...

        

    lblTiempoPartida['text'] = "Tiempo de partida: "+str(contador1)+':'+str(contador)

    proceso=lblTiempoPartida.after(1000, tiempoPartida,(contador+1),(contador1))

            

    return 



def terminarPartida():

    '''

    Función: Eventos que suceden cuando se presiona el boton de terminar la partida (btnTerminar).

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''

    terminarTurno()

    global proceso

    lblTiempoPartida.after_cancel(proceso)

    btnIniciar.config(state='normal')

    lblTiempoPartida['text'] = "Tiempo de partida: "



    return



def terminarTurno():

    '''

    Función: Eventos que suceden cuando se presiona el boton de terminar turno(btnFinalizar).

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''

    global proceso2

    global ponerNombre

    

    nombres=eventoBotonJuego()

    

    if ponerNombre==True:

        jugador.set('Jugador: '+nombres[0])

        ponerNombre=False

    else:

        nombres=eventoBotonJuego()

        ponerNombre=True

    

    

    lblTiempoTurno.after_cancel(proceso2)

   # btnIniciar.config(state='normal')

    lblTiempoTurno['text'] = "Tiempo de Turno: "



    return



def eventoBotonJuego():

    '''

    Función: Toma los nombres de los entrys, y recorta hasta 5 caracteres.

    Entradas: Ninguna.

    Salidas: Ninguna.

    '''

    nombreA=''

    nombreB=''

    j1=jugador1.get()

    j2=jugador2.get()



    while len(j1)<5 or len(j2)<5:

        j1+="_"

        j2+="_"

        

    for i in range(0,5):

        nombreA+=j1[i]

        nombreB+=j2[i]

        



    jugadorA.set('Jugador '+nombreA+':')

    jugadorB.set('Jugador '+nombreB+':')



    return [nombreA, nombreB]

#-------------Programa Principal-------------#



#creacion de la Ventana

ventana = Tk()

ventana.title("PalabraCraft")

ventana.config(bg="#cfc27c")

ventana.iconbitmap("scrabble.ico")

ventana.resizable(0,0)



miFont = font.Font (family ='Californian FB', size = 13, weight = "bold")

fichasFont = font.Font(family ='Cambria', size = 12, weight = "bold")

tituloFont = font.Font(family ='Chiller', size = 20, weight = "bold")

letra =  font.Font(family ='Fixedsys', size = 45, weight = "bold")

letraMasPeq =  font.Font(family ='Fixedsys', size = 18, weight = "bold")

letraMasPeq2 =  font.Font(family ='Fixedsys', size = 13)



#---------------Se crean filas y columnas en la ventana---------------#

for i in range(0, 30):   #se crean 4 columnas.

    ventana.columnconfigure(i, weight=1)

for i in range(0, 30):  #se crean 8 filas.

    ventana.rowconfigure(i, weight=1)

    

#---------------Solo es para ver las rayitas de la ventana-------------#

f=30

c=30

for k in range(0, f+1):

    frame= Frame(ventana, width=1, height=700, bg="#424242")

    frame.grid(row= 0, column=k, rowspan=f, sticky= "NW")

for k in range(0, c+1):

    frame= Frame(ventana, width=1050, height=1, bg="#424242")

    frame.grid(row= k, column=0, columnspan=c, sticky= "NW")





#------------------------WIDGETS DE VENTANAINICIAL---------------#

frame1 = Frame(ventana, bg= '#FE9A2E')

for i in range(0, 30):

    frame1.columnconfigure(i, weight=1)

for i in range(0, 30):

    frame1.rowconfigure(i, weight=1)





imagen=PhotoImage(file="imgscrabble.png")

lblImagen=Label(frame1,image=imagen, bg='#FE9A2E')



jugador1=StringVar()

jugador1.set("") #Se declara la variable que permite el set y get del Entry

entJugador1=Entry(frame1,font=letraMasPeq2,textvariable=jugador1)



jugador2=StringVar()

jugador2.set("") #Se declara la variable que permite el set y get del Entry

entJugador2=Entry(frame1,font=letraMasPeq2, textvariable=jugador2)



lblnombreJuego=Label(frame1,font=letra,text='Palabra Craft', bg='#FE9A2E')

lblJugador1=Label(frame1,font=letraMasPeq2,text='Nombre del jugador 1: ', bg='#FE9A2E')

lblJugador2=Label(frame1,font=letraMasPeq2,text='Nombre del jugador 2: ', bg='#FE9A2E')



entJugador2.bind('<Return>', onEnter)

btnJugar=Button(frame1,font=letraMasPeq,text="Jugar",command=lambda:ventanaJuego())



#------------------------WIDGETS DE VENTANAJUEGO---------------#

frame2 = Frame(ventana, bg= '#FE9A2E')

for i in range(0, 30):

    frame2.columnconfigure(i, weight=1)

for i in range(0, 30):

    frame2.rowconfigure(i, weight=1)





imagen2=PhotoImage(file="award.png")

lblImagen2=Label(frame2,image=imagen2, bg='#FE9A2E')



#Frames

frameTablero = Frame(frame2,bg='#FE9A2E')

frameFichas = Frame(frame2,bg='#FE9A2E')



#Botones 

btnIniciar = Button(frame2,font=miFont,text="   Iniciar Partida  ",command=lambda:tiempoPartida())

btnTerminar = Button(frame2,font=miFont,text="Terminar Partida",state="disabled",command=lambda:terminarPartida())

btnComenzar = Button(frame2,font=miFont,text="    Iniciar Turno   ",state="disabled", command=lambda:tiempoTurno())

btnFinalizar = Button(frame2,font=miFont,text=" Finalizar Turno ", state="disabled", command=lambda:terminarTurno())

btnImprimir = Button(frame2,font=miFont,text=" Imprimir matriz ")



#Labels

lblLetrasD = Label(frame2,font=miFont,text="Letras Disponibles:",bg='#FE9A2E')

lblTitulo = Label(frame2,font=letraMasPeq,text="Palabra Craft",bg='#FE9A2E')

lblTiempoPartida = Label(frame2,font=letraMasPeq2,text='Tiempo de partida:',bg='#FE9A2E')

lblTiempoTurno = Label(frame2,font=letraMasPeq2,text='Tiempo de turno:',bg='#FE9A2E')



lblTurno = Label(frame2,font=letraMasPeq2,text="Turno: 0",bg='#FE9A2E')

jugador=StringVar()

jugador.set('Jugador: nombre')

lblJugador = Label(frame2,font=letraMasPeq2,textvariable=jugador,bg='#FE9A2E')



lblPuntaje = Label(frame2,font=letraMasPeq2,text='Puntaje: ',bg='#FE9A2E')



jugadorA=StringVar()

jugadorA.set('Jugador nombreA:')

jugadorB=StringVar()

jugadorB.set('Jugador nombreB: ')

lblJugadorA = Label(frame2,font=letraMasPeq2,textvariable=jugadorA,bg='#FE9A2E')

lblJugadorB = Label(frame2,font=letraMasPeq2,textvariable=jugadorB,bg='#FE9A2E')



puntajeA=StringVar()

puntajeA.set('0')

puntajeB=StringVar()

puntajeB.set('0')

lblPuntajeA = Label(frame2,font=letraMasPeq2,textvariable=puntajeA,bg='#FE9A2E')

lblPuntajeB = Label(frame2,font=letraMasPeq2,textvariable=puntajeA,bg='#FE9A2E')



#ventanaJuego()

ventanaInicial()

ventana.mainloop()
