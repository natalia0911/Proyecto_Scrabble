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
#import sys
#sys.setdefaultencoding('utf-8')


#variables globales
global matriz
global letras
global archivo
global fichasJ1
global fichasJ2
global turno 
global tiempoPartida
global tiempoTurno
global proceso
global proceso2
global fichasSelecionadas
global matrizBotones
global cantFichasMin

matriz=[]
letras=[]
archivo = []
fichasJ1 = []
fichasJ2 = []
turno = True
tiempoPartida = ''
tiempoTurno = ''
proceso=0
proceso2=0
fichasSelecionadas = []
matrizBotones = []
cantFichasMin = 0

#Definición de Funciones


    
def ventanaInicial():

    '''
    Función:  Colocar objetos en el frame 1 y frame sobre la ventana.
    Entradas: Ninguna.
    Salidas: .
    '''

    frame2.grid_remove()
    frame1.grid(row=0,column=0, rowspan=30, columnspan=30, sticky=(E,W,N,S))
    lblImagen.place(x=170,y=420)
    lblnombreJuego.grid(row=5,column=10, rowspan=5, columnspan=9, sticky=(E,W,N,S))
    lblJugador1.grid(row=13,column=9, rowspan=1, columnspan=4, sticky=(N,S))
    lblJugador2.grid(row=15,column=9, rowspan=1, columnspan=4, sticky=(N,S))
    entJugador1.grid(row=13,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))
    entJugador2.grid(row=15,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))
    btnJugar.grid(row=18,column=13, rowspan=1, columnspan=6, sticky=(E,W,N,S))
    


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
    frame1.grid_remove()
    
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
    


   
def crearMatriz():

    '''
    Función:  Crea una matriz 15x15.
    Entradas: Ninguna.
    Salidas: Llama a cargarBD().
    '''

    for i in range(0,15):
        matriz.append([])
        matrizBotones.append([])
        for j in range(0,15):
            matriz[i].append(0)
            matrizBotones[i].append(0)

            
    return cargarBD()


def mostrarMatriz():
    '''
    Función:  Muestra el estado actual de la matriz.
    Entradas: Ninguna.
    Salidas: Imprime la matriz del tablero.
    '''
    for l in matriz:
        print(l)
    return

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

        for i in archivo:
            i[2]=i[2].rstrip(";\n")
            
        return crearListaLetras()

    except:

        return "Ocurrió un error"


def crearListaLetras():
    '''
    Función: Crea una lista con la cantidad de cada tipo de ficha disponible.
    Entradas: Ninguna.
    Salidas: Llama a la funcion darFichas().
    '''
        
    global letras
    global cantFichasMin
    
    for i  in range(len(archivo)):
        mulLetra=archivo[i][0]*int(archivo[i][1])
        letras+=list(mulLetra)

    cantFichasMin=round((len(letras)/100)*30)
    
    return darFichas()


def ganadorPPFichas(cantActual):
    '''
    Función: Dice quien es el ganador en el momento en que se gastaron el 70% de las fichas iniciales.
    Entradas: Ninguna.
    Salidas: Llama a la funcion darLetras().
    '''

    global cantFichasMin
    nombres=eventoBotonJuego()
    
    if cantActual <= cantFichasMin:
        ganadorPorTiempo()
        
    print("El 30% de las fichas es ",cantFichasMin)
    print("Cantidad de fichas actual ",cantActual)


def darFichas():
    '''
    Función: Crea dos listas con las 7 letras iniciales para cada jugador.
    Entradas: Ninguna.
    Salidas: Llama a la funcion darLetras().
    '''


    for i in range(0,7):
        letra = letras[random.randint(0,len(letras)-1)]
        fichasJ1.append(letra)
        
    for i in range(0,7):
        letra = letras[random.randint(0,len(letras)-1)]
        fichasJ2.append(letra)

        
    print("Todas las fichas disponibles: ",letras)
    print("Fichas jugador1: ",fichasJ1)
    print("Fichas jugador2: ",fichasJ2) 

    for k in fichasJ1:
        letras.remove(k)
    for l in fichasJ2:
        letras.remove(l)
        
    print("")
    print("Todas las fichas disponibles ahora(después de borrar las 7): ",letras)

    ganadorPPFichas(len(letras))
    
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

    tamanno= 1
    for i in archivo:

        texto.insert(tk.INSERT,i[0]+"="+i[2]+"\n")  #Inserta la letra y la cantidad en el TEXT.
        if len(i[0])>tamanno:
            tamanno = len(i[0])
            texto.config(width=len(i[0]+"="+i[2]))
            
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
            
            matrizBotones[i][j] = Button(frameTablero,width=2,height=1,bg='#81BEF7',text='')
            matrizBotones[i][j].grid(row=i, column=j)
            matrizBotones[i][j].bind('<Button-1>',lambda e,i=i,j=j,casilla=matrizBotones[i][j]: colocarFichasJugador(i,j,casilla))

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
        matriz[filaL][columnaL] = 1


    for i in range(mulPalabra):  # se crea una cantidad de 2-6 mul de palabra
        filaP=random.randint(0,14)
        columnaP=random.randint(0,14)
        if matriz[filaP][columnaP]== 0:

            matriz[filaP][columnaP]= 2
            

    for l in matriz:
        print(l)


    return colocarFichasJugador()


def colocarFichaTablero(i,j,casilla,ficha,fichas):


    '''
    Función: Coloca las fichas que el jugador seleccionó,en el tablero. 
    Entradas: i,j,casilla,ficha,fichas.
    Salidas: Ninguna.
    '''

    print(i,j)
    
    for k in range(len(matriz)):
        for l in range(len(matriz)):
            casilla.config(state='disabled')
            


    if casilla["text"] == "":
        if ficha["text"]!= "":
            
            letraSeleccionada=ficha["text"]  #Es la letra
            comodin = matriz[i][j]           #Es lo que hay en la casilla (0,1,2)
            actualizarPuntaje(letraSeleccionada,comodin)   #Llama a esta funcion 
            
            matriz[i][j] = ficha["text"]

            for l in matriz:
                print(l)
            casilla.config(text=ficha["text"],bg = "#fff1c7")
            fichas.remove(ficha["text"])
            print(fichas)
            ficha.config(text="")



def actualizarPuntaje(letraSeleccionada,comodin):
    '''
    Función: Agrega puntos a una lista.
    Entradas: letraSeleccionada,comodin.
    Salidas: Ninguna.
    '''
    global fichasSelecionadas
   
    
    print('La letra seleccionada fue: ', letraSeleccionada,'y lo que hay en la casilla es:', comodin)

    for n in archivo:
        if n[0]==letraSeleccionada:
            puntos=int(n[2])

    if comodin == 1:
        print("Multiplicador de letra")
        fichasSelecionadas.append(puntos*2)
        
    elif comodin == 2:
        print("Multiplicador de palabra")
      
        fichasSelecionadas = [3]+fichasSelecionadas
        fichasSelecionadas.append(puntos)
         
    else:
         
        fichasSelecionadas.append(puntos)

    return 


def darPuntaje():
    
    '''
    Función: Actualizar los puntajes.
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''
    global fichasSelecionadas
    
    print(fichasSelecionadas)
    puntaje = 0
    if fichasSelecionadas !=[]:
        if fichasSelecionadas[0]==3:
            for i in fichasSelecionadas[1:]:
                print(i)
                
                puntaje+= i 
            puntaje = puntaje*2
        
        else:
            for i in fichasSelecionadas:
                print(i)
                puntaje+= i 
            
        if turno == False:
            puntaje+=int(puntajeA.get())
            print("puntaje: ",puntaje)
            puntajeA.set(str(puntaje))

        if turno == True:
            puntaje+=int(puntajeB.get())
            print("puntaje: ",puntaje)
            puntajeB.set(str(puntaje))

        fichasSelecionadas = []

    return


def colocarFichasJugador(i,j,casilla):    
    '''
    Función: Coloca las letras de los jugadores en las fichas. 
    Entradas: Ninguna.
    Salidas: Llama a la funcion crearCasillasBonus().
    '''

    #EQUIS CON ESTO

    for k in range(0,15):
        for n in range(0,15):
            if casilla["text"]!= "":
                casilla.config(bg="#fff1c7")
                
            if matrizBotones[i][j] == matrizBotones[k][n]:
                matrizBotones[i][j].config(bg="#A70202")
            else:
                matrizBotones[k][n].config(state='disabled')
                matrizBotones[k][n].config(bg='#81BEF7')
                
            
            
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

def actualizarFichas():
    """
    Funcion:  Actualiza las fichas del jugador si tiene menos de 7
    Entrada: .
    Salida:  .
    """
    global fichasJ1
    global fichasJ2
    
    if turno == True:
        fichas = fichasJ1

    elif turno == False:
        fichas = fichasJ2

    fichasN=[]
    if len(fichas)<7:
        for i in range(7-len(fichas)):
            letra = letras[random.randint(0,len(letras)-1)]
            fichasN.append(letra)
        for k in fichasN:
                letras.remove(k)

    fichas += fichasN
    print(letras)
    print(fichas)

    ganadorPPFichas(len(letras))
    return 

def bitacora():
    """
    Funcion: 
    Entrada:
    Salida:
    """
    f= open("Bitacora","w")
    f.write("\n"+numTurno.get()+"-"+jugador.get()[9:]+"-")
    
    


def iniciarTurno():
    '''
    Función: Llama a la función que inicializa el turno.
    Entradas: Ninguna.
    Salidas: Funcion tiempoTurno(contador=30,contador1=0).
    '''
    global turno
    btnComenzar.config(state='disabled')
    btnTerminar.config(state='normal')
    btnFinalizar.config(state='normal')


    nombres=eventoBotonJuego()
    
    if turno == True:
        jugador.set('Jugador: '+nombres[0])
        numTurno.set("Turno: "+ str(1))
        
    return tiempoTurno(contador=30,contador1=0)

def tiempoTurno(contador=30,contador1=0):

    '''
    Función: Crear un cronometro para el tiempo de cada turno.
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''

    global proceso2

        
    if contador == 0:
        lblTiempoTurno['text'] = "Tiempo de Turno: 0:0"
        messagebox.showinfo(" ", "Fin de su turno.")
        return  cambiarTurno()  #solo lo puse para parar el tiempo a los 30 s...

    lblTiempoTurno['text'] = "Tiempo de Turno: "+str(contador1)+':'+str(contador)

    proceso2=lblTiempoTurno.after(1000, tiempoTurno,(contador-1),(contador1))

            
    return 

def terminarTurno():

    '''
    Función: Termina el turno pero llama a cambiarTurno() y el tiempo se reinicia.
    Entradas: Ninguna.
    Salidas: cambiarTurno().
    '''
    
    global proceso2

    btnComenzar.config(state='disabled')

    lblTiempoTurno.after_cancel(proceso2)
    btnIniciar.config(state='disabled')
    lblTiempoTurno['text'] = "Tiempo de Turno: 0:30"
    
     
    
    return cambiarTurno()

def pararTiempoTurno():
    
    '''
    Función: Para el tiempo de turno definitivamente.
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''
    global proceso2

    lblTiempoTurno.after_cancel(proceso2)
    btnIniciar.config(state='disabled')
    lblTiempoTurno['text'] = "Tiempo de Turno: "

    return

def iniciarPartida():
    '''
    Función: Llama a la función que inicializa la partida.
    Entradas: Ninguna.
    Salidas: tiempoPartida(contador=0,contador1=15)
    '''
        
    btnIniciar.config(state='disabled')  #se deshabilita una vez iniciada la partida
    btnComenzar.config(state='normal')
    btnTerminar.config(state='disabled')
    
    return tiempoPartida(contador=0,contador1=1)
    
def tiempoPartida(contador=0,contador1=1):

    '''
    Función: Crear un cronometro para el tiempo de cada partida.
    Entradas: contador y contador1 (enteros)inicializados en 0.
    Salidas: Ninguna.
    '''

    global proceso

    if contador == 0:
        contador=59
        contador1-=1

    if contador1 == 0 and contador == 1:
        lblTiempoPartida['text'] = "Tiempo de partida: "
        messagebox.showinfo(" ", "Fin de la partida.")  
        return ganadorPorTiempo()


    lblTiempoPartida['text'] = "Tiempo de partida: "+str(contador1)+':'+str(contador)
    proceso=lblTiempoPartida.after(1000, tiempoPartida,(contador-1),(contador1))   

    return 



def terminarPartida():

    '''
    Función: Eventos que suceden cuando se presiona el boton de terminar la partida (btnTerminar).
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''
    pararTiempoTurno()
    lblTiempoPartida.after_cancel(proceso)
    
    nombres=eventoBotonJuego()
    nom = jugador.get()
    
    if nom[9:] == nombres[0]:
        print("El Ganador es: ", nombres[1])
        messagebox.showinfo("Ganador", "El ganador es: "+nombres[1])  #ESTO, EVENTUALMENTE PODRÍA SER MÁS FINO
    else:
        print("El Ganador es: ", nombres[0])
        messagebox.showinfo("Ganador", "El ganador es: "+nombres[0])

    btnIniciar.config(state='normal')
    btnFinalizar.config(state='disabled')
    btnTerminar.config(state='disabled')
    lblTiempoPartida['text'] = "Tiempo de partida: "
    jugador2.set("")
    jugador1.set("")
    jugador.set('Jugador: ')
    numTurno.set("Turno: 0")

    return ventana.destroy()
     



def pararTiempoPartida():
    '''
    Función: Para el tiempo de partida.
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''
    

    lblTiempoPartida.after_cancel(proceso)
    lblTiempoPartida['text'] = "Tiempo de partida: "
    pararTiempoTurno()
    btnIniciar.config(state='normal')
    btnFinalizar.config(state='disabled')
    jugador.set('Jugador: ')
    numTurno.set("Turno: 0")
    jugador2.set("")
    jugador1.set("")
    jugadorA.set('Jugador :')
    jugadorB.set('Jugador :')
    puntajeA.set('0')
    puntajeB.set('0')

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

def ganadorPorTiempo():

    '''
    Función: Decir quién es el ganador cuando se termina tiempo de la partida.
    Entradas: Ninguna.
    Salidas: retorna la funcion pararTiempoPartida().
    '''
    
    nombres=eventoBotonJuego()
    puntosA = int(puntajeA.get())
    puntosB = int(puntajeB.get())

    if puntosA==puntosB:
        messagebox.showinfo("Ganador", "Ocurrió un empate")
    elif puntosA>puntosB:
        messagebox.showinfo("Ganador", "El ganador de la partida es: "+nombres[0])
    else:
        messagebox.showinfo("Ganador", "El ganador de la partida es: "+nombres[1])


    btnIniciar.config(state='normal')
    btnFinalizar.config(state='disabled')
    pararTiempoPartida()
    pararTiempoTurno()

    return ventana.destroy()
    

def cambiarTurno():

    '''
    Función: Se realizan todos los cambios necesarios al terminar un turno.
    Entradas: Ninguna.
    Salidas: Ninguna.
    '''
    global turno
    nombres=eventoBotonJuego()
    numeroTurno = numTurno.get()
    
    if turno == False:
        jugador.set('Jugador: '+nombres[0])
        if (int(numeroTurno[7:])) == 20: 
       
            return ganadorPorTiempo()
     
        else:   
            numTurno.set("Turno: "+ str(int(numeroTurno[7:])+1))
            turno = True
            
    elif turno == True:
        jugador.set('Jugador: '+nombres[1])
        numTurno.set("Turno: "+ str(int(numeroTurno[7:])))
        turno = False

    actualizarFichas()

    darPuntaje()
    
    
    
    tiempoTurno(contador=30,contador1=0)

    
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


#--------------Se crean filas y columnas en la ventana---------------#
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

btnIniciar = Button(frame2,font=miFont,text="   Iniciar Partida  ",command=lambda:iniciarPartida())
btnTerminar = Button(frame2,font=miFont,text="Terminar Partida",state="disabled",command=lambda:terminarPartida())
btnComenzar = Button(frame2,font=miFont,text="    Iniciar Turno   ",state="disabled", command=lambda:iniciarTurno())
btnFinalizar = Button(frame2,font=miFont,text=" Finalizar Turno ", state="disabled", command=lambda:terminarTurno())
btnImprimir = Button(frame2,font=miFont,text=" Imprimir matriz ", command=lambda:mostrarMatriz())

#Labels

lblLetrasD = Label(frame2,font=miFont,text="Letras Disponibles:",bg='#FE9A2E')
lblTitulo = Label(frame2,font=letraMasPeq,text="Palabra Craft",bg='#FE9A2E')
lblTiempoPartida = Label(frame2,font=letraMasPeq2,text='Tiempo de partida:',bg='#FE9A2E')
lblTiempoTurno = Label(frame2,font=letraMasPeq2,text='Tiempo de turno:',bg='#FE9A2E')

numTurno = StringVar()
numTurno.set("Turno: 0")
lblTurno = Label(frame2,font=letraMasPeq2,textvariable=numTurno,bg='#FE9A2E')

jugador = StringVar()
jugador.set('Jugador:')
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
lblPuntajeB = Label(frame2,font=letraMasPeq2,textvariable=puntajeB,bg='#FE9A2E')



#ventanaJuego()

ventanaInicial()

ventana.mainloop()
