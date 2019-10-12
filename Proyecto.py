#
#
#
#
#Importacion de librerias
import random

global matriz
global listMulPalabra
global listMulLetra
global dicValoresLetras

matriz=[]
listMulPalabra=[]
listMulLetra=[]
dicValoresLetras={}

def crearMatriz():
    '''
    Función:
    Entradas:
    Salidas:
    '''
    
    for i in range(0,15):
        matriz.append([])
        for j in range(0,15):
            matriz[i].append(0)
            
    return generaTablero()


def generaTablero():
    '''
    Función:
    Entradas:
    Salidas:
    '''

    mulPalabra=random.randint(2,6) #cantidad de multiplicadores de palabra
    
    for i in range(mulPalabra):
        filaP=random.randint(0,14)
        columnaP=random.randint(0,14)
        listMulPalabra.append([filaP,columnaP])
        matriz[filaP][columnaP]= 2
        
    for i in range(0,10): # Hay 10 multiplicadores de letra
        filaL=random.randint(0,14)
        columnaL=random.randint(0,14)
        listMulLetra.append([filaL,columnaL])
        matriz[filaL][columnaL]= 2
        
    for l in matriz:
        print(l)
        
    print(listMulPalabra)#Podemos ver una lista con coordenadas de los multiplicadores
    print(listMulLetra)
    
    return tomarValoresLetras()

def tomarValoresLetras():
    '''
    Función: Toma los valores de las letras, del archivo txt que contiene los valores.
    Entradas:
    Salidas:
    '''
    dicValoresLetras["A"]=1
    dicValoresLetras["B"]=2
    dicValoresLetras["C"]=3
    dicValoresLetras["D"]=4
    dicValoresLetras["F"]=5
    dicValoresLetras["G"]=6
    dicValoresLetras["H"]=7
    #dicValoresLetras={"A":1,"B":4,"C":2,"D":6,"E":1,"F":5} si se hace asi no lo imprime en el principal :(
    #print(dicValoresLetras)

def decirLetra(pletra,pfila,pcolumna):
    '''
    Función: 
    Entradas:
    Salidas:
    '''
    valorLetra=0
    laLetra=''
    for letra,valor in dicValoresLetras.items():
        if letra==pletra:
            valorLetra=valor
            laLetra=letra
    
    return ponerLetraEnTablero(laLetra,valorLetra,pfila,pcolumna)


def ponerLetraEnTablero(laLetra,valorLetra,pfila,pcolumna):
    '''
    Función: 
    Entradas:
    Salidas:
    '''

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if pfila==i and pcolumna==j:
                if matriz[i][j]==2:
                    valorLetra*=2
                
                matriz[i][j]=laLetra  
                ''' Para ver si lo hacia bien
                print(i,j)
                print(matriz[i][j])
                print(valorLetra)
                print(laLetra)'''

                
    print("Puntos ganados",valorLetra)  #Solo para un posible funcionamiento
    for l in matriz:
        print(l)
        
    
    
#Programa principal#
crearMatriz()
print(dicValoresLetras)  
letra=input("Ingrese digite la letra: ")
fila=int(input("Digite la fila: "))
columna=int(input("Digite la columna: "))
print(decirLetra(letra,fila,columna))

