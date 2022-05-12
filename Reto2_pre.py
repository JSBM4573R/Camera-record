"""
El programa recibirá 3 parámetros:
La distancia en metros que separa dos cámaras.
El actual récord de velocidad para ese trayecto en (Km/h).
El tiempo en segundos que tarda el piloto en recorrer el trayecto. """

"""

El programa imprimirá una línea con dos valores: el primer valor corresponde a la 
velocidad media del piloto en el trayecto evaluado en (km/h) y con un número decimal; 
el segundo valor indicará sí el piloto superó el récord o no. Se debe considerar lo siguiente:
Imprimirá VELOCIDAD NORMAL si el piloto no superó el récord.
Imprimirá NUEVO RECORD si se superó la velocidad registrada en el récord actual en menos de un 25%.
Imprimirá ENTREVISTA si el récord fue superado en un 25% o más de la velocidad registrada en el récord actual. 
En este caso se realizará una entrevista en medios deportivos.
Debido a que los sistemas pueden fallar y registrar valores errados, 
(por ejemplo, indicando que el tiempo que ha tardado el piloto es negativo) 
en esos casos, se deberá imprimir únicamente VALORES NEGATIVOS.

"""
x_metros_camaras, actual_record, tiempo_segundos = input().split(" ")
x_metros_camaras = float(x_metros_camaras)
actual_record = float(actual_record)
tiempo_segundos = float(tiempo_segundos)

x_km = float(x_metros_camaras/1000)
tiempo_horas = float(tiempo_segundos/3600)
velocidad_media = float(x_km/tiempo_horas)

if x_metros_camaras > 0 or actual_record > 0 or tiempo_segundos > 0:
    if velocidad_media < actual_record:
        print (round(velocidad_media, 1), "VELOCIDAD NORMAL")
    elif actual_record < velocidad_media < (actual_record + actual_record * 0.25):
        print (round(velocidad_media, 1), "NUEVO RECORD")
    elif velocidad_media > (actual_record + actual_record * 0.25):
        print (round(velocidad_media, 1), "ENTREVISTA")
else:
    print("VALORES NEGATIVOS")



    