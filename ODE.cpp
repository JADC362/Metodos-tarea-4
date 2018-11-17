//Importacion de librerias
#include<iostream>
#include <fstream>
#include<cmath>
#include <sstream>
#include <algorithm> 
#include <vector>
#include <math.h> 
using namespace std;

//Definicion de variables globales
//Como se hace uso de vectores, la convencion de componentes sera sera A = {Ax,Ay}
float static c = 0.2;
float static m  = 0.2;
float static PI = 3.14159265359;
vector<float> g;
float static ht = 0.001; //Intervalo de tiempo entre punto y punto
float static timeS = 3.0; //Tiempo total de simulacion
int N = (int) timeS/ht; 

vector<float> f[2];
vector<float> x0;
vector<float> v0;
vector<int> contador;

void calcularFuncion(vector<float> y0,vector<float> y1){
	float magY1 = sqrt(pow(y1.at(0),2)+pow(y1.at(1),2));
	vector<float> tempY1;
	float tempY1_x = -g.at(0)-(c/m)*(magY1)*y1.at(0);
	float tempY1_y = -g.at(1)-(c/m)*(magY1)*y1.at(1);
	tempY1.push_back(tempY1_x);
	tempY1.push_back(tempY1_y);
	f[0]=y1;
	f[1]=tempY1;
}

//Calcula los movimientos de un proyectil a partir de unas condiciones iniciales establecidas, un angulo y el nombre del archivo en donde guardar los datos 
float calcularMovimientoProyectil(float angulo,string archivoNombre){
	//Condiciones iniciales para V0
	v0.clear();
	v0.push_back(300*cos(angulo*PI/180.0));
	v0.push_back(300*sin(angulo*PI/180.0));

	//Inicializando y asignando el valor inicial a Y = {X,V}
	vector<float> Y[N][2];
	Y[0][0]=x0;
	Y[0][1]=v0;


	//Creacion flujo de datos para archivo datos.dat
	ofstream datos;
	if(archivoNombre == "datosODE2.dat"){
		//contador.clear();
		datos.open(archivoNombre.c_str(), ios::out | ios::app);
	}
	else{
		datos.open(archivoNombre.c_str());
	}

	datos<<"Angulo:"<<angulo<<endl;

	float distanciaRecorrida = 0;
	//Calculo de movimiento y velocidad del proyectil
	for (int i = 1; i < N; ++i)
	{
		//Calculo de k1
		vector<float> k1[2];
		calcularFuncion(Y[i-1][0],Y[i-1][1]);
		k1[0] = f[0];
		k1[1] = f[1];

		//Calculo de k2
		vector<float> k2[2];

		vector<float> tempY0_k2;
		float tempY0_k2_x = (Y[i-1][0]).at(0)+(ht/2.0);
		float tempY0_k2_y = (Y[i-1][0]).at(1)+(ht/2.0);
		tempY0_k2.push_back(tempY0_k2_x);
		tempY0_k2.push_back(tempY0_k2_y);

		vector<float> tempY1_k2;
		float tempY1_k2_x = (Y[i-1][1]).at(0)+((k1[1]).at(0))*(ht/2.0);
		float tempY1_k2_y = (Y[i-1][1]).at(1)+((k1[1]).at(1))*(ht/2.0);
		tempY1_k2.push_back(tempY1_k2_x);
		tempY1_k2.push_back(tempY1_k2_y);

		calcularFuncion(tempY0_k2,tempY1_k2);
		k2[0] = f[0];
		k2[1] = f[1];

		//Calculo de k3
		vector<float> k3[2];

		vector<float> tempY0_k3;
		float tempY0_k3_x = (Y[i-1][0]).at(0)+(ht/2.0);
		float tempY0_k3_y = (Y[i-1][0]).at(1)+(ht/2.0);
		tempY0_k3.push_back(tempY0_k3_x);
		tempY0_k3.push_back(tempY0_k3_y);

		vector<float> tempY1_k3;
		float tempY1_k3_x = (Y[i-1][1]).at(0)+((k2[1]).at(0))*(ht/2.0);
		float tempY1_k3_y = (Y[i-1][1]).at(1)+((k2[1]).at(1))*(ht/2.0);
		tempY1_k3.push_back(tempY1_k3_x);
		tempY1_k3.push_back(tempY1_k3_y);

		calcularFuncion(tempY0_k3,tempY1_k3);
		k3[0] = f[0];
		k3[1] = f[1];

		//Calculo de k4
		vector<float> k4[2];

		vector<float> tempY0_k4;
		float tempY0_k4_x = (Y[i-1][0]).at(0)+(ht);
		float tempY0_k4_y = (Y[i-1][0]).at(1)+(ht);
		tempY0_k4.push_back(tempY0_k4_x);
		tempY0_k4.push_back(tempY0_k4_y);

		vector<float> tempY1_k4;
		float tempY1_k4_x = (Y[i-1][1]).at(0)+((k3[1]).at(0))*(ht);
		float tempY1_k4_y = (Y[i-1][1]).at(1)+((k3[1]).at(1))*(ht);
		tempY1_k4.push_back(tempY1_k4_x);
		tempY1_k4.push_back(tempY1_k4_y);

		calcularFuncion(tempY0_k4,tempY1_k4);
		k4[0] = f[0];
		k4[1] = f[1];

		//Creacion de pendiente
	 	float slope0X = (1.0/6.0)*((k1[0]).at(0)+2.0*(k2[0]).at(0)+2.0*(k3[0]).at(0)+(k4[0]).at(0));
	 	float slope0Y = (1.0/6.0)*((k1[0]).at(1)+2.0*(k2[0]).at(1)+2.0*(k3[0]).at(1)+(k4[0]).at(1));
	 	float slope1X = (1.0/6.0)*((k1[1]).at(0)+2.0*(k2[1]).at(0)+2.0*(k3[1]).at(0)+(k4[1]).at(0));
	 	float slope1Y = (1.0/6.0)*((k1[1]).at(1)+2.0*(k2[1]).at(1)+2.0*(k3[1]).at(1)+(k4[1]).at(1));
	 	
	 	vector<float> slope0;
	 	slope0.push_back(slope0X);
	 	slope0.push_back(slope0Y);

	 	vector<float> slope1;
	 	slope1.push_back(slope1X);
	 	slope1.push_back(slope1Y);

	 	vector<float> Y0;
	 	vector<float> Y1;	

	 	Y0.push_back((Y[i-1][0]).at(0)+ht*slope0.at(0));
	 	Y0.push_back((Y[i-1][0]).at(1)+ht*slope0.at(1));
	 	Y1.push_back((Y[i-1][1]).at(0)+ht*slope1.at(0));
	 	Y1.push_back((Y[i-1][1]).at(1)+ht*slope1.at(1));

	 	if ((Y[i-1][0]).at(1) < 0)
	 	{
	 		contador.push_back(i);
	 		break;
	 	}
	 	
		Y[i][0]=Y0;
		Y[i][1]=Y1;

		distanciaRecorrida += sqrt(pow(Y[i][0].at(0)-Y[i-1][0].at(0),2)+pow(Y[i][0].at(1)-Y[i-1][0].at(1),2));	
		datos<<"t="<<i*ht<<" , X-x="<<(Y[i-1][0]).at(0)<<" , X_y="<<(Y[i-1][0]).at(1)<<" , V-x="<<(Y[i-1][1]).at(0)<<" , V_y="<<(Y[i-1][1]).at(1)<<"\n";
	}
	datos.close();
	return distanciaRecorrida;
}

int main(){
	g.push_back(0.0);
	g.push_back(10.0);	

	x0.push_back(0.0);
	x0.push_back(0.0);

	//Parte uno
	float angulo = 45.0;
	float distancia45 = calcularMovimientoProyectil(angulo,"datosODE1.dat");
	cout<<"(Punto 1) La distancia recorrida es: "<<distancia45<<"m"<<endl;

	//Punto dos
	float distanciasAngulos[7];
	for (int i = 1; i <= 7; ++i)
	{
		angulo=10*i;
		distanciasAngulos[i-1]=calcularMovimientoProyectil(angulo,"datosODE2.dat");
	}
	
	ofstream datos;
	datos.open("datosODE2.dat", ios::out | ios::app);
	datos<<contador.at(1)<<","<<contador.at(2)<<","<<contador.at(3)<<","<<contador.at(4)<<","<<contador.at(5)<<","<<contador.at(6)<<","<<contador.at(7)<<endl;
	datos.close();
	float distanciaMaxima = 0;
	int anguloMaximo = 10;
	for (int i = 0; i < 7; ++i)
	{
		if (distanciasAngulos[i]>distanciaMaxima)
		{
			distanciaMaxima = distanciasAngulos[i];
			anguloMaximo = (i+1)*10;
		}
	}
	cout<<"(Punto 2) La distancia maxima recorrida es: "<<distanciaMaxima<<"m"<<" y se da para un angulo de "<<anguloMaximo<<" grados."<<endl;
	return 0;
}