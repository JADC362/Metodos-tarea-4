//Importacion de librerias
#include<iostream>
#include<cmath>
#include <vector>
#include <math.h> 
using namespace std;
//Definicion de variables globales
//Como se hace uso de vectores, la convencion de componentes sera sera A = {Ax,Ay}
float static c = 0.2;
float static m  = 0.2;
//float static g[2] = {0.0,10.0};
vector<float> g;
int static ht = 0.01; //Intervalo de tiempo entre punto y punto
float static timeS = 5; //Tiempo total de simulacion
int N = (int) timeS/ht; 

vector<float> f[2];

void funY(vector<float> y0,vector<float> y1){
	float magY1 = sqrt(pow(y1.at(0),2)+pow(y1.at(1),2));
	vector<float> tempY1;
	float tempY1_x = -g.at(0)-(c/m)*(magY1)*y1.at(0);
	float tempY1_y = -g.at(1)-(c/m)*(magY1)*y1.at(1);
	tempY1.push_back(tempY1_x);
	tempY1.push_back(tempY1_y);
	f[0]=y1;
	f[1]=tempY1;
}

void calcularMovimientoProyectil(vector<float> x0,vector<float> v0){
	//Inicianliazdo y asignando el valor inicial a Y = {X,V}
	vector<float> Y[N][2];
	Y[0][0]=x0;
	Y[0][1]=v0;

	for (int i = 1; i < N; ++i)
	{
		//Calculo de k1
		vector<float> k1[2];
		funY(Y[i-1][0],Y[i-1][1]);
		k1[0] = f[0];
		k1[1] = f[1];

		//Calculo de k2
		vector<float> k2[2];

		vector<float> tempY0_k2;
		float tempY0_k2_x = (Y[i-1][0]).at(0)+(ht/2);
		float tempY0_k2_y = (Y[i-1][0]).at(1)+(ht/2);
		tempY0_k2.push_back(tempY0_k2_x);
		tempY0_k2.push_back(tempY0_k2_y);

		vector<float> tempY1_k2;
		float tempY1_k2_x = (Y[i-1][1]).at(0)+((k1[1]).at(0))*(ht/2);
		float tempY1_k2_y = (Y[i-1][1]).at(1)+((k1[1]).at(1))*(ht/2);
		tempY1_k2.push_back(tempY1_k2_x);
		tempY1_k2.push_back(tempY1_k2_y);

		funY(tempY0_k2,tempY1_k2);
		k2[0] = f[0];
		k2[1] = f[1];

		//Calculo de k3
		vector<float> k3[2];

		vector<float> tempY0_k3;
		float tempY0_k3_x = (Y[i-1][0]).at(0)+(ht/2);
		float tempY0_k3_y = (Y[i-1][0]).at(1)+(ht/2);
		tempY0_k3.push_back(tempY0_k3_x);
		tempY0_k3.push_back(tempY0_k3_y);

		vector<float> tempY1_k3;
		float tempY1_k3_x = (Y[i-1][1]).at(0)+((k2[1]).at(0))*(ht/2);
		float tempY1_k3_y = (Y[i-1][1]).at(1)+((k2[1]).at(1))*(ht/2);
		tempY1_k3.push_back(tempY1_k3_x);
		tempY1_k3.push_back(tempY1_k3_y);

		funY(tempY0_k3,tempY1_k3);
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

		funY(tempY0_k4,tempY1_k4);
		k4[0] = f[0];
		k4[1] = f[1];

	 	//slope = (1.0/6.0)*(k1+2.0*k2+2.0*k3+k4);
		//Y[i][0]=Y[i-1][0]+ht*slope[0];
	}
}

int main(){
	g.push_back(0.0);
	g.push_back(10.0);	

	vector<float> x0;
	x0.push_back(0.0);
	x0.push_back(0.0);

	vector<float> v0;
	v0.push_back(300*cos(45));
	v0.push_back(300*sin(45));

	//calcularMovimientoProyectil(x0,v0);
	return 0;
}