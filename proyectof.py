from os import system
system("cls")
import numpy as np
import datetime
from datetime import timedelta
#plazasparqueadero = 75
car = 50
mot = 25

matrizcar1a10 = np.array ('[ c1-c2-c3-c4-c5-c6-c7-c8-c9-c10]')#,[ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],[ 21, 22, 23, 24, 25 ,26 ,27, 28, 29, 30],[ 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],[ 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
matrizcar11a20 = np.array ('[ c11-c12-c13-c14-c15-c16-c17-c18-c19-c20]')
matrizcar21a30 = np.array ('[ c21-c22-c23-c24-c25-c26-c27-c28-c29-c30]')
matrizcar31a40 = np.array ('[ c31-c32-c33-c34-c35-c36-c37-c38-c39-c40]')
matrizcar41a50 = np.array ('[ c41-c42-c43-c44-c45-c46-c47-c48-c49-c50]') 
matrizmot1a10 = np.array ('[ m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]')
matrizmot11a20 = np.array ('[ m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]')
matrizmot21a25 = np.array ('[ m21, m22, m23, m24, m25]')

print("-------------- parqueadero de carros ------------------")
print (matrizcar1a10)
print("                                           ")
print (matrizcar11a20)
print ("                                          ")
print (matrizcar21a30)
print("                                           ")
print (matrizcar31a40)
print("                                           ")
print (matrizcar41a50)
print("------------------Parqueadero de motos -----------------")
print (matrizmot1a10)
print("                                           ")
print (matrizmot11a20)
print("                                           ")
print (matrizmot21a25)

#caromoto = input(" ¿Carro o moto? ")
seleccion = input(" ¿Carro o moto? \n Presione -1- para carro o -2- para moto ")
if seleccion == "1":
    print("Parqueadero de carros")
    placadecar = input("Ingrese la placa del carro :")
elif seleccion == "2":
    print("Parqueadero de motos")
    placademot = input("Ingrese la placa del moto :")


#hora de entrada y salida vehicular

horadeentrada = datetime.datetime.now()
print ("La hora de entrada del vehiculo es: ", horadeentrada.hour,":",horadeentrada.minute)
print("**Tiene una hora gratis en la estancia del parqueadero.** ")

#actualizar??

tiempodeestadia = int(input("Ingrese el tiempo en minutos  que estuvo en el parqueadero: "))
#from datetime import datetime, timedelta; resultado = datetime.now() + timedelta(hours=3)
tiempoestadia = (datetime.datetime.now() - tiempodeestadia)

if horadeentrada > 60:
    print("Estadía gratuita de 1 hora, vuelva pronto. ")
elif (horadeentrada - tiempoestadia >=60):
    print("El costo de  la estadía es: $",tiempoestadia*0.1)


""" salidadevehi = (placadecar or placademot)
horasalida= input(print("Ingrese la placa del vehiculo ingresado anteriormente para su salida: "))
print("La placa de  salida del vehiculo es: ", salidadevehi) """





