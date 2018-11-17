#Graficacion datos ODE

#Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)
    
x = np.arange(0,N,1)
y = np.arange(0,N,1)
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
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)
    
x = np.arange(0,N,1)
y = np.arange(0,N,1)
x,y = np.meshgrid(x, y)
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
    inicioContador += N+1
    finalContador += N+1
    matrizTiempo.append(matrizTemp)
    
x = np.arange(0,N,1)
y = np.arange(0,N,1)
x,y = np.meshgrid(x, y)
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
