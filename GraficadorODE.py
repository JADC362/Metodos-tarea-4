#Graficacion datos ODE

#Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt

#Obtencion y clasificacion de datos para los valores de movimiento de proyecto de los angulo 45 
datos = np.genfromtxt("datosODE1.dat",dtype=None,delimiter="\n")
datosTi=np.zeros([len(datos)])
datosDx=np.zeros([len(datos)])
datosDy=np.zeros([len(datos)])
datosVx=np.zeros([len(datos)])
datosVy=np.zeros([len(datos)])
angulo = datos[0].decode("UTF8").split(":")[1]
for i in range(1,len(datos)):  
    datosTi[i] = float((datos[i]).decode("UTF8").split(",")[0].split("=")[1])
    datosDx[i] = float((datos[i]).decode("UTF8").split(",")[1].split("=")[1])
    datosDy[i] = float((datos[i]).decode("UTF8").split(",")[2].split("=")[1])
    datosVx[i] = float((datos[i]).decode("UTF8").split(",")[3].split("=")[1])
    datosVy[i] = float((datos[i]).decode("UTF8").split(",")[4].split("=")[1])

plt.figure()
plt.plot(datosDx,datosDy,label="Angulo:"+angulo)
plt.title("Movimiento de un proyectil")
plt.ylabel("Posicion Y")
plt.xlabel("Posicion X")
plt.legend()
plt.savefig("proyectilAngulo45.pdf",bbox_inches="tight")

#Obtencion y clasificacion de datos para los valores de movimiento de proyecto de los angulo 10,20,30,40,50,60,70
datos = np.genfromtxt("datosODE2.dat",dtype=None,delimiter="\n",skip_footer=1)
contadores = np.genfromtxt("datosODE2.dat",delimiter=",",skip_header=len(datos))
matrizDatos = []
inicioContador = 1;
finalContador = int(contadores[0]);
for i in range(7):
    matrizDatos.append([])
    for j in range(5):
        matrizDatos[i].append(np.zeros([int(contadores[i])-1]))
    for j in range(inicioContador,finalContador):
        matrizDatos[i][0][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[0].split("=")[1])
        matrizDatos[i][1][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[1].split("=")[1])
        matrizDatos[i][2][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[2].split("=")[1])
        matrizDatos[i][3][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[3].split("=")[1])
        matrizDatos[i][4][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[4].split("=")[1])
    inicioContador += int(contadores[i]);
    if i != 6:
        finalContador += int(contadores[i+1]);

plt.figure()
for i in range(7):
    plt.plot(matrizDatos[i][1],matrizDatos[i][2],label="Angulo:"+str(10*(i+1)))
plt.title("Movimiento de un proyectil")
plt.ylabel("Posicion Y")
plt.xlabel("Posicion X")
plt.legend()
plt.savefig("proyectilDiferentesAngulos.pdf",bbox_inches="tight")