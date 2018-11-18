#Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Graficacion datos ODE

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


#Graficacion datos PDE

#Vector de tiempo y temperatura promedio
vectorTiempoF = []
vectorTempPF = []
vectorTiempoA = []
vectorTempPA = []
vectorTiempoP = []
vectorTempPP = []

#Obtencion y clasificacion de datos del archivo datosF para condiciones fijas
datos = np.genfromtxt("datosPDEF.dat",None,skip_header=1)
infoDatos = (np.genfromtxt("datosPDEF.dat",skip_footer=(len(datos)-1),dtype=None))[0].decode("UTF8").split(",")
matrizTiempo = [] #Matriz contenedora de matrices del estado de temperaturas en el tiempo
T = int(infoDatos[1]) #Contador de tiempo total
N = int(infoDatos[3]) #Contador de espacio x=y total
inicioContador = 1;
finalContador = N+1
for i in range(T):
    matrizTemp = np.zeros([N,N]) #Matriz de temperatura para un tiempo dado
    for j in range(inicioContador,finalContador):
        infoLinea = datos[j].decode("UTF8").split(",")
        for k in range(N):
            matrizTemp[j-inicioContador][k]=float(infoLinea[k])
    vectorTiempoF.append(float(datos[inicioContador-1].decode("UTF8").split(",")[1]))
    vectorTempPF.append(float(datos[inicioContador-1].decode("UTF8").split(",")[3]))
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)
    
x = np.arange(0,N)*0.01
y = np.arange(0,N)*0.01
x,y = np.meshgrid(x, y)
#Grafica de temperatura en la grilla X Y, para tiempo 0
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[0], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondFi1.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondFi2.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo 2*T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)*2/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondFi3.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[T-1], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondFi4.pdf",bbox_inches="tight")


#Obtencion y clasificacion de datos del archivo datosA para condiciones abiertas
datos = np.genfromtxt("datosPDEA.dat",None,skip_header=1)
infoDatos = (np.genfromtxt("datosPDEA.dat",skip_footer=(len(datos)-1),dtype=None))[0].decode("UTF8").split(",")
matrizTiempo = [] #Matriz contenedora de matrices del estado de temperaturas en el tiempo
T = int(infoDatos[1]) #Contador de tiempo total
N = int(infoDatos[3]) #Contador de espacio x=y total
inicioContador = 1;
finalContador = N+1
for i in range(T):
    matrizTemp = np.zeros([N,N]) #Matriz de temperatura para un tiempo dado
    for j in range(inicioContador,finalContador):
        infoLinea = datos[j].decode("UTF8").split(",")
        for k in range(N):
            matrizTemp[j-inicioContador][k]=float(infoLinea[k])
    vectorTiempoA.append(float(datos[inicioContador-1].decode("UTF8").split(",")[1]))
    vectorTempPA.append(float(datos[inicioContador-1].decode("UTF8").split(",")[3]))
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)
    
#Grafica de temperatura en la grilla X Y, para tiempo 0
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[0], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondAb1.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondAb2.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo 2*T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)*2/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondAb3.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[T-1], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondAb4.pdf",bbox_inches="tight")

# Obtencion y clasificacion de datos del archivo datosP para condiciones periodicas
datos = np.genfromtxt("datosPDEP.dat",None,skip_header=1)
infoDatos = (np.genfromtxt("datosPDEP.dat",skip_footer=(len(datos)-1),dtype=None))[0].decode("UTF8").split(",")
matrizTiempo = [] #Matriz contenedora de matrices del estado de temperaturas en el tiempo
T = int(infoDatos[1]) #Contador de tiempo total
N = int(infoDatos[3]) #Contador de espacio x=y total
inicioContador = 1;
finalContador = N+1
for i in range(T):
    matrizTemp = np.zeros([N,N]) #Matriz de temperatura para un tiempo dado
    for j in range(inicioContador,finalContador):
        infoLinea = datos[j].decode("UTF8").split(",")
        for k in range(N):
            matrizTemp[j-inicioContador][k]=float(infoLinea[k])
    vectorTiempoP.append(float(datos[inicioContador-1].decode("UTF8").split(",")[1]))
    vectorTempPP.append(float(datos[inicioContador-1].decode("UTF8").split(",")[3]))
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)


#Grafica de temperatura en la grilla X Y, para tiempo 0
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[0], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondPe1.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondPe2.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo 2*T/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[int((T-1)*2/3)], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondPe3.pdf",bbox_inches="tight")

#Grafica de temperatura en la grilla X Y, para tiempo T
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, matrizTiempo[T-1], rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("temperaturaCondPe4.pdf",bbox_inches="tight")

plt.figure()
plt.plot(vectorTiempoF,vectorTempPF,label="Fijas")
plt.plot(vectorTiempoA,vectorTempPA,label="Abiertas")
plt.plot(vectorTiempoP,vectorTempPP,label="Periodicas")
plt.title("Temperatura promedio en la calcita en el tiempo")
plt.ylabel("Temperatura [K]")
plt.xlabel("Tiempo[s]")
plt.legend(loc=0)
plt.savefig("temperaturaPromedioTiempo.pdf",bbox_inches="tight")

plt.figure()
plt.plot(vectorTiempoF,vectorTempPF,label="Fijas")
plt.plot(vectorTiempoA,vectorTempPA,label="Abiertas")
plt.plot(vectorTiempoP,vectorTempPP,label="Periodicas")
plt.title("Temperatura promedio en la calcita en el tiempo")
plt.ylabel("Temperatura [K]")
plt.xlabel("Tiempo[s]")
plt.xscale('log')
plt.legend(loc=0)
plt.savefig("temperaturaPromedioTiempoLog.pdf",bbox_inches="tight")