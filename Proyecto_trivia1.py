""" Bienvenidos al proyecto Trivia 

Autor: Juan Emanuel Choque

Version: 1.0

Descripcion:
Este programa tiene el fin de entretener al usuario mediante preguntas que otorgan un puntaje 
y un tiempo a vencer correspondiente al mejor jugador guardado.

"""

import csv


# Buscamos retornar el alias del jugador y no mostrar tanto codigo en pantalla.

def jugadores(numero_jugadores):
    
    while numero_jugadores > 0:
        if numero_jugadores == 2:
            print("Por favor ingrese su nombre jugador 1 ")
            nombre_1 = str(input())
            print("Por favor ingrese el nombre del jugador 2")
            nombre_2 = str(input())
            
            print("{} y {} son los jugadores de hoy".format(nombre_1,nombre_2))
            print("{} y {} deben saber que sus resultados se comparan con los jugadores anteriores".format(nombre_1,nombre_2))
            return nombre_1 and nombre_2
            break
            
        elif numero_jugadores == 1:
            print("Por favor ingrese su nombre o alias")
            jugador_1 = str(input())
            print("Buena Suerte", jugador_1)
            return jugador_1
            break
        else:
            print("Ingrese de nuevo la cantidad de jugadores, por el momento lo maximo son 2 por juego")
            jugadores = int(input())


def categorias():
    
    categorias_a_jugar = []
    categorias_a_jugar.append("netflix")
    categorias_a_jugar.append("cultura mundial")
    
    print("Por favor seleccione la categoria en la cual quiere competir :", categorias_a_jugar)

    categoria = str(input()) 
    print("La categoria elegida es :", categoria)
    if categoria == categorias_a_jugar[0]:
        numero = 0
    elif categoria == categorias_a_jugar[1]:
        numero = 1    
    else:
        print("no hay n")
    return numero

def pregunta(numero):
    csvfile = open("preguntas.csv")
    data = list(csv.DictReader(csvfile))
    
    numero_de_preguntas = len(data)
    fila = 0
    columna = "pregunta"
    if numero == 0:    
        while fila < numero_de_preguntas:   
            opcion_1 = "respuesta_1"
            opcion_2 = "respuesta_2"
            opcion_3 = "respuesta_3"
            opcion_4 = "respuesta_4"
            print("La pregunta es :", data[fila][columna])
            print("Sus opciones son :\n","1",data[fila][opcion_1],"2",data[fila][opcion_2],"3",data[fila][opcion_3],"4",data[fila][opcion_4])
            fila += 1 
            break      
    else:
        print("Estamos trabajando en ello ") 
    
    csvfile.close()


def respuesta():
    csvfile = open("preguntas.csv")
    data_1 = list(csv.DictReader(csvfile))

    puntaje = 0
    vidas = 3
    
    fila = 0
    columna = "respuesta_correcta"
    if vidas > 0:
        print("ingrese su respuesta")
        decision = int(input())
        if decision == int(data_1[fila][columna]):
            print("su respuesta a sido correcta")
            puntaje += 20
            fila += 1
            
            
        else:
            print("Incorrecto")
            puntaje += 0
            vidas -= 1
            fila += 1
    csvfile.close()
    return puntaje

     

""" Categorias:
 Se podria decir que usaremos netflix como recurso y la cultura mundial
 Animacion
 Peliculas de Terror,etc
 Documentales
 Comedia
 Religion
 datos de interes
 Escritores Famosos y Directores de obras famosas


def record_jugadores(nombre,puntaje):
    
    records_anteriores = {"max": 20, "pepe":15}
    key = nombre
    value = puntaje
    records_anteriores[key] = value
    
    for i in records_anteriores.items():
        
    return maximo_record

respuestas_incorrectas = 0
x = 0
valor_preguntas = 20 
vidas_jug_1 = 3
vidas_jug_2 = 3    
"""


if __name__=='__main__':

    print("Bienvenido a Trivia Mundo!!, para comenzar ingrese el numero de jugadores ")
    
    nombres = jugadores(int(input()))
    tema = categorias()
    cuestionario = pregunta(tema)
    puntaje = respuesta()
    """maximo_record = record_jugadores(nombres)"""
    
    print("Gracias por jugar en el proyecto Trivia 1") 
    print("Su puntuacion es :",puntaje)   
    """ print("El record es de :", maximo_record)"""






