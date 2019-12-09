import problema_espacio_estados as probe
import búsqueda_espacio_estados as buse
import copy

class Mapa:
    def __init__(self, celdas):
        self.celdas = celdas
    
    def tamanoEjeX(self):
        return len(self.celdas[0]) #Número de celdas del primer array de celdas (Solo eje X)
    
    def tamanoEjeY(self):
        return len(self.celdas) #Número de celdas del primer array de celdas (Solo eje Y)
    
    def tipoCelda(self, f, c):
        return self.celdas[f][c] #te devuelve el valor de una celda

mapaEjemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                     [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
                     [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
                     [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

posInicial = (5,0) #Se pone primero el eje Y, luego el X. La posición 0 del Eje Y es arriba del todo y se mueve hacia abajo
posFinal = (0,9)

def suma(estado): # valor de las celdas escogidas en los estados
    return mapaEjemplo.tipoCelda(estado[0], estado[1])
#-----------------------------------------------------------
def puedeAbajo(estado):#Devuelve true si al moverse hacia abajo no se sale del mapa y debajo no hay una casilla de agua
    return estado[0] < mapaEjemplo.tamanoEjeY() -1 and mapaEjemplo.tipoCelda(estado[0]+1, estado[1]) != 0

def mueveAbajo(estado): #nuevo estado
    return estado[0]+1, estado[1]

desplazamientoAbajo = probe.Acción("Moverse hacia abajo", puedeAbajo, mueveAbajo,
suma) #Comprueba que puede moverse hacia abajo, se mueve y obtiene el valor de la casilla
#-----------------------------------------------------------
def puedeDerecha(estado):#Devuelve true si al moverse a la derecha no se sale del mapa y a la derecha no hay una casilla de agua
    return estado[1] < mapaEjemplo.tamanoEjeX() -1 and mapaEjemplo.tipoCelda(estado[0], estado[1] + 1) != 0

def mueveDerecha(estado): #nuevo estado
    return estado[0], estado[1] + 1

desplazamientoDerecha = probe.Acción("Moverse hacia la derecha", puedeDerecha, mueveDerecha,
suma) #Comprueba que puede moverse a la derecha, se mueve y obtiene el valor de la casilla
#-----------------------------------------------------------
def puedeArriba(estado):#Devuelve true si al moverse hacia arriba no se sale del mapa y arriba no hay una casilla de agua.
    return estado[0] > 0 and mapaEjemplo.tipoCelda(estado[0]-1, estado[1]) != 0 #Ponemos un "-" pues va hacia arriba

def mueveArriba(estado): #nuevo estado
    return estado[0]-1, estado[1] # Se pone "-" por la misma razón

desplazamientoArriba = probe.Acción("Moverse hacia arriba", puedeArriba, mueveArriba,
suma) #Comprueba que puede moverse a la izquierda, se mueve y obtiene el valor de la casilla
#-----------------------------------------------------------
def puedeIzquierda(estado):#Devuelve true si al moverse a la izquierda no se sale del mapa y a la izquierda no hay una casilla de agua.
    return estado[1] > 0 and mapaEjemplo.tipoCelda(estado[0], estado[1] - 1) != 0 #Ponemos un "-" pues va hacia la izquierda

def mueveIzquierda(estado): #nuevo estado
    return estado[0], estado[1] - 1 # Se pone "-" por la misma razón

desplazamientoIzquierda = probe.Acción("Moverse hacia la izquierda", puedeIzquierda, mueveIzquierda,
suma) #Comprueba que puede moverse a la izquierda, se mueve y obtiene el valor de la casilla


problemaEstados = probe.ProblemaEspacioEstados([desplazamientoAbajo, desplazamientoDerecha, desplazamientoArriba,
desplazamientoIzquierda], posInicial, [posFinal])

solucionOptima = buse.BúsquedaÓptima()
print("\n")
print(solucionOptima.buscar(problemaEstados))
