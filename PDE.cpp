//Importacion de librerias
#include<iostream>
#include<cmath>
#include <math.h> 
#include <fstream>
#include <sstream>
using namespace std;

//Constantes
static float PI = 3.14159265359;

static float L = 0.5; //Longitud placa
static float d = 0.1; //Diametro barrila

static float ka = 1.62; //[m^2 /s]
static float Cp = 820; //[J/(kg K)]
static float rho = 2710; //[kg/m^3]
static float v = ka/(Cp*rho); //Coeficiente de difusion

static float dx = 0.01; //dx = dy
static float alpha = 0.2;
static float dt = alpha*pow(dx,2)/v;

int N =  L/dx;
int NBarra = d/dx;
int NCalcita = (int) (N*N)-(PI*pow(NBarra,2));
int TF = 1000;
int TA = 1000;
int TP = 1000;

static float tempBarra = 100+273;
static float tempIni = 10+273;

void ecuacionDifusionCondicionesF(string nombreArchivo){
	//Creacion archivo de datos
	ofstream datos;
	datos.open(nombreArchivo.c_str());

	float matrizPasado[N][N];
	float matrizPresente[N][N];

	float tempPromedio = tempIni;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqCirc <= pow(d/2,2))
			{
				matrizPasado[i][j]=tempBarra;
			}
			else{
				matrizPasado[i][j]=tempIni;
			}
		}
	}
	datos << "T,"<<TF<<",N,"<<N<<"\n";
	for (int k = 0; k < TF; ++k)
	{
		datos << "Tiempo,"<<k*dt<<",TempPromedio,"<<tempPromedio<<"\n";
		tempPromedio = 0;
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{	
				if ((i > 0  && i < (N-1)) && (j > 0 && j < (N-1)))
				{
					float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqCirc > pow(d/2,2))
					{
						matrizPresente[i][j]=alpha*(matrizPasado[i+1][j]+matrizPasado[i-1][j]+matrizPasado[i][j+1]+matrizPasado[i][j-1])+((1-4*alpha)*matrizPasado[i][j]);
						tempPromedio += matrizPresente[i][j];
					}
					else{
						matrizPresente[i][j] = tempBarra;
					}
				}
				else{
					matrizPresente[i][j] = tempIni;
					tempPromedio += matrizPresente[i][j];
				}
				datos << matrizPasado[i][j]<< ",";
			}
			datos << "\n";
		}
		tempPromedio = tempPromedio/(NCalcita);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{
				matrizPasado[i][j]=matrizPresente[i][j];
			}
		}
	}
	datos.close();
}

void ecuacionDifusionCondicionesA(string nombreArchivo){
	//Creacion archivo de datos
	ofstream datos;
	datos.open(nombreArchivo.c_str());

	float matrizPasado[N][N];
	float matrizPresente[N][N];

	float tempPromedio = tempIni;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqCirc <= pow(d/2,2))
			{
				matrizPasado[i][j]=tempBarra;
			}
			else{
				matrizPasado[i][j]=tempIni;
			}
		}
	}
	datos << "T,"<<TA<<",N,"<<N<<"\n";
	for (int k = 0; k < TA; ++k)
	{
		datos << "Tiempo,"<<k*dt<<",TempPromedio,"<<tempPromedio<<"\n";
		tempPromedio = 0;
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{	
				if ((i > 0  && i < (N-1)) && (j > 0 && j < (N-1)))
				{
					float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqCirc > pow(d/2,2))
					{
						matrizPresente[i][j]=alpha*(matrizPasado[i+1][j]+matrizPasado[i-1][j]+matrizPasado[i][j+1]+matrizPasado[i][j-1])+((1-4*alpha)*matrizPasado[i][j]);
						tempPromedio += matrizPresente[i][j];
					}
					else{
						matrizPresente[i][j] = tempBarra;
					}
				}
				else{
					for (int l = 0; l < N; ++l)
					{
						matrizPresente[0][l]=matrizPresente[1][l];
						matrizPresente[N-1][l]=matrizPresente[N-2][l];
						matrizPresente[l][0]=matrizPresente[l][1];
						matrizPresente[l][N-1]=matrizPresente[l][N-2];
					}
					tempPromedio += matrizPresente[i][j];
				}
				datos << matrizPasado[i][j]<< ",";
			}
			datos << "\n";
		}
		tempPromedio = tempPromedio/(NCalcita);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{
				matrizPasado[i][j]=matrizPresente[i][j];
			}
		}
	}
	datos.close();
}

void ecuacionDifusionCondicionesP(string nombreArchivo){
	//Creacion archivo de datos
	ofstream datos;
	datos.open(nombreArchivo.c_str());

	float matrizPasado[N][N];
	float matrizPresente[N][N];

	float tempPromedio = tempIni;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqCirc <= pow(d/2,2))
			{
				matrizPasado[i][j]=tempBarra;
			}
			else{
				matrizPasado[i][j]=tempIni;
			}
		}
	}
	datos << "T,"<<TP<<",N,"<<N<<"\n";
	for (int k = 0; k < TP; ++k)
	{
		datos << "Tiempo,"<<k*dt<<",TempPromedio,"<<tempPromedio<<"\n";
		tempPromedio = 0;
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{	
				if ((i > 0  && i < (N-1)) && (j > 0 && j < (N-1)))
				{
					float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqCirc > pow(d/2,2))
					{
						matrizPresente[i][j]=alpha*(matrizPasado[i+1][j]+matrizPasado[i-1][j]+matrizPasado[i][j+1]+matrizPasado[i][j-1])+((1-4*alpha)*matrizPasado[i][j]);
						tempPromedio += matrizPresente[i][j];
					}
					else{
						matrizPresente[i][j] = tempBarra;
					}
				}
				else{
					for (int l = 0; l < N; ++l)
					{
						matrizPresente[0][l]=matrizPresente[N-1][l];
						matrizPresente[l][0]=matrizPresente[l][N-1];
					}
					tempPromedio += matrizPresente[i][j];
				}
				datos << matrizPasado[i][j]<< ",";
			}
			datos << "\n";
		}
		tempPromedio = tempPromedio/(NCalcita);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{
				matrizPasado[i][j]=matrizPresente[i][j];
			}
		}
	}
	datos.close();
}

int main(){
	ecuacionDifusionCondicionesF("datosPDEF.dat");
	ecuacionDifusionCondicionesA("datosPDEA.dat");
	ecuacionDifusionCondicionesP("datosPDEP.dat");
	return 0;
}