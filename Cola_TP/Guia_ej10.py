from stack import Stack
from Queue import Queue
from datetime import time

notificaciones = Queue()
pila_aux = Stack()

notificaciones.arrive({"Hora": time(14,30),
                       "App": "instagram",
                       "mensaje": "tienes una nueva solicitud de seguimiento"})

notificaciones.arrive({"Hora": time(15,20),
                       "App": "twitter",
                       "mensaje": "fulano: recomendaciones de cursos de python virtuales?"})

notificaciones.arrive({"Hora": time(11,38),
                       "App": "twitter",
                       "mensaje": "fulano dio me gusta a tu twit"})

notificaciones.arrive({"Hora": time(12,25),
                       "App": "instagram",
                       "mensaje": "fualana ha dado me gusta a tu historia"})

notificaciones.arrive({"Hora": time(22,30),
                       "App": "instagram",
                       "mensaje": "fulana ah dado me gusta a tu publicacion"})

notificaciones.arrive({"Hora": time(18,30),
                       "App": "facebook",
                       "mensaje": "tienes una nueva sugerencia de amistad"})

notificaciones.arrive({"Hora": time(10,36),
                       "App": "twitter",
                       "mensaje": "fulanito: aprendi python viendo cursos en youtube"})

notificaciones.arrive({"Hora": time(11,30),
                       "App": "facebook",
                       "mensaje": "tienes una nueva solicitud de amistad"})

#funcion para restaurar la cola
def restaurar_cola(cola, pila):
    temp = Stack()
    while pila:
        temp.push(pila.pop()) 
    while temp:
        cola.arrive(temp.pop())  

#funcion para eliminar notificaciones de facebook
def eliminar_noti(notificaciones):
    while notificaciones:
        notificacion = notificaciones.attention()
        if notificacion["App"] != "facebook".lower():
            pila_aux.push(notificacion)
    restaurar_cola(notificaciones, pila_aux)  

#funcion para mostrar twits que mencionan python
def twitter_py(notificaciones):
    palabra = "python"
    while notificaciones:
        notificacion = notificaciones.attention()
        pila_aux.push(notificacion)
        if palabra in notificacion["mensaje"].lower():
            print(notificacion)
    restaurar_cola(notificaciones, pila_aux)    

#funcion para mostrar las notificaciones entre las 11:43 y 15:57
def notis_por_horario(notificaciones):
    pila_temp = Stack()
    contador = 0
    while notificaciones:
        notificacion = notificaciones.attention()
        pila_aux.push(notificacion)
        if time(11, 43) <= notificacion["Hora"] <= time(15, 57):
            pila_temp.push(notificacion)
            contador += 1
    restaurar_cola(notificaciones, pila_aux)  
    print("notificaciones entre las 11:43 y las 15:57")
    pila_temp.show()
    print("cantidad:")
    print(contador)  

#ejecucion
eliminar_noti(notificaciones) 
print("notificaciones (sin facebook):")         
notificaciones.show()
print()
print("notificaciones de twitter que mencionan python:")
twitter_py(notificaciones)
print()
notis_por_horario(notificaciones)
