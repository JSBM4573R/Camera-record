x_metros_camaras, actual_record, tiempo_segundos = input().split(" ")
x_metros_camaras = float(x_metros_camaras)
actual_record = float(actual_record)
tiempo_segundos = float(tiempo_segundos)

x_km = float(x_metros_camaras/1000)
tiempo_horas = float(tiempo_segundos/3600)
velocidad_media = float(x_km/tiempo_horas)

if x_metros_camaras > 0 and actual_record > 0 and tiempo_segundos > 0:
    if velocidad_media < actual_record:
        print (round(velocidad_media, 1), "VELOCIDAD NORMAL")
    elif actual_record < velocidad_media < (actual_record + actual_record * 0.25):
        print (round(velocidad_media, 1), "NUEVO RECORD")
    elif velocidad_media > (actual_record + actual_record * 0.25):
        print (round(velocidad_media, 1), "ENTREVISTA")
else:      
    print("VALORES NEGATIVOS")