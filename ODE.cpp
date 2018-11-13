//Importacion de librerias
#include<iostream>
#include<cmath>

//Definicion de variables globales
//Como se hace uso de vectores, la convencion de componentes sera sera A = {Ax,Ay}
float static c = 0.2;
float static m  = 0.2;
float static g[2] = {0.0,10.0};
int static ht = 0.01; //Intervalo de tiempo entre punto y punto
float static timeS = 5; //Tiempo total de simulacion
int N = (int) timeS/ht; 

void calcularMovimientoProyectil(float x0[2],float v0[2]){
	//Inicializando vectores Y0 - desplazamiento y Y1 - velocidad
	float Y0[N][2];
	float Y1[N][2];
	
	//Guardando condiciones iniciales
	Y0[0][0]=x0[0];
	Y0[0][1]=x0[1];

	Y1[0][0]=v0[0];
	Y1[0][1]=v0[1];

}

int main(){
	float x0[2]={0,0};
	float v0[2]={300*cos(45),300*sin(45)};
	calcularMovimientoProyectil(x0,v0);
	return 0;
}