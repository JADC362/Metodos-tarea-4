Resultados_hw4.pdf: Resultados_hw4.tex proyectilAngulo45.pdf
	pdflatex Resultados_hw4.tex
	rm Resultados_hw4.log
	rm Resultados_hw4.aux
	rm proyectilAngulo45.pdf proyectilDiferentesAngulos.pdf temperaturaCondFi1.pdf temperaturaCondAb1.pdf temperaturaCondPe1.pdf temperaturaCondFi2.pdf temperaturaCondAb2.pdf temperaturaCondPe2.pdf temperaturaCondFi3.pdf temperaturaCondAb3.pdf temperaturaCondPe3.pdf temperaturaCondFi4.pdf temperaturaCondAb4.pdf temperaturaCondPe4.pdf
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
