//Importacion de librerias
#include<iostream>
#include<cmath>
#include <math.h> 
#include <fstream>
#include <sstream>
using namespace std;

//Constantes
static float L = 50.0; //Longitud placa
static float d = 10.0; //Diametro barrila

static float ka = 1.62; //[m^2 /s]
static float Cp = 820; //[J/(kg K)]
static float rho = 2710; //[kg/m^3]
static float v = ka/(Cp*rho); //Coeficiente de difusion

static float dx = 1; //dx = dy
static float alpha = 0.1;
static float dt = alpha*pow(dx,2)/v;

int N = (int) L/dx;
int NBarra = (int) d/dx;
int T = 100;

void ecuacionDifusionCondicionesF(string nombreArchivo){
	//Creacion archivo de datos
	ofstream datos;
	datos.open(nombreArchivo.c_str());

	float matrizPasado[N][N];
	float matrizPresente[N][N];

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			float eqCirc = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqCirc <= pow(d/2,2))
			{
				matrizPasado[i][j]=100;
			}
			else{
				matrizPasado[i][j]=10;
			}
		}
	}
	datos << "T,"<<T<<",N,"<<N<<"\n";
	for (int k = 0; k < T; ++k)
	{
		datos << "Tiempo:"<<k*dt<<"\n";
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
					}
					else{
						matrizPresente[i][j] = 100;
					}
				}
				else{
					matrizPresente[i][j] = 10;
				}
				datos << matrizPasado[i][j]<< ",";
			}
			datos << "\n";
		}
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
	ecuacionDifusionCondicionesF("datosF.dat");
	return 0;
}