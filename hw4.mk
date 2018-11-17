Resultados_hw4.pdf: proyectilAngulo45.pdf

proyectilAngulo45.pdf: datosODE1.dat datosPDEF.dat
	python Plots_hw4.py
	rm datosODE1.dat datosODE2.dat datosPDEF.dat datosPDEA.dat datosPDEP.dat

datosODE1.dat: ODE.cpp
	g++ ODE.cpp
	./a.out
	rm a.out

datosPDEF.dat: PDE.cpp
	g++ PDE.cpp
	./a.out
	rm a.out
