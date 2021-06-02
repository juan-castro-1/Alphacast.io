# Alphacast.io
Consultat test interview

---
Esta carpeta es como generalmente trabajo con Scripts: Carpeta con Input (Data), Carpeta con Output (Plots, Tablas, etc), Scripts divididos por función (ej: 1.DataCleaning, 2.Analysis, etc), un Script CONSOLIDADO (contiene todos los Scripts anteriores) y un README.txt que explica como funciona
---

RUN: Hay dos formas de correr el archivo

1- Abrir el 2.Analysis.py y correrlo paso a paso. Desde este se corre el archivo 1.DataCleaning.py sin necesidad de abrirlo y se cargan todas las variables del mismo para el análisis.

2- Trabajar directamente con el CONSOLIDADO.py que contiene el script de los otros dos archivos .py en uno. 


Carpetas:

-Data: carpeta con los excels a usar

-Output: carpeta donde se exportan los Plots, Tablas, etc que en este caso no se uso

Scripts:
-1.DataCleaning: todo el proceso de cargar y data managment previo al analysis
-2.Analysis: todo el analysis pedido, en Plots
-CONSOLIDADO: un archivo con los dos archivos anteriores unidos
