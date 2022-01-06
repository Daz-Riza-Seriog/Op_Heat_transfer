# Code made for Sergio Andres Diaz Ariza
# 03 November 2021
# License MIT
# Heat Operations: Python Program

import numpy as np
import matplotlib.pyplot as plt
#PROPIEDADES PLACA COLECTORA DE ACERO INOXIDABLE 316

a=0.00000348;   #Difusividad térmica AISI 316 [=] m^2/s
h=10;           #Coefciente de transferencia [=] W / m^2 * °C       POR VERSE
ro_s=8238;      #Densidad [=] kg/m^3
Cp_s=468;       #Calor específico [=] J/kg * °C
k_s=13.4;       #Conductividad térmica [=] W/m * °C
Ac=0.0015;      #Área superficial que hace convección            POR VERSE
T_inf=30;       #Temperatura de ambiente [=] °C
T_wat=25;       #Temperatura inicial del agua a la entrada del tubo [=] °C
h_agua=200;

m_a=0.318;                  #Velocidad del agua [=] m/s
a_esp=(2*0.1)/(2*0.1*0.15); #Área específica de la placa [=] m^(-1)

q_rad=1.05;     #Calor absorbido por la placa [=] W
v_s= 0.03;      #Volumen de la placa [=] m^3

x0=0.1;  #Longitud del ancho [=] m
y0=2;    #Longitud del largo [=] m

N=20;   #Número de nodos/fila
M=20;   #Número de nodos/columna

dx=x0/(N-1);  #Diferencial de longitud
dy=y0/(M-1); #Diferencial de longitud

function F= funciones_ct(time, x)


for i=N+2:N * M - N - 1 # Para nodos internos, 22 al 379
    F(i, 1) = a * ((x(i - 1) - 2 * x(i) + x(i + 1)) / (dx) ^ 2 + (x(i - N) - 2 * x(i) + x(i + N)) / (dx) ^ 2) + (
            q_rad / Cp_s * ro_s * v_s); # Función por la que se rigen


for i=1:N :
    F(i, 1) = -k_s / (ro_s * Cp_s) * (x(i) - x(i + N)) / dy * Ac - h * 100000 / (ro_s * Cp_s) * Ac * (
            x(i) - T_inf); # Primera fila(Acá hay conveccion)
    F(N * N - N + i, 1) = -k_s / (ro_s * Cp_s) * (x(N * N - N + i) - x(N * N - N + i - N)) / dy * Ac - h * 100000 / (
            ro_s * Cp_s) * Ac * (x(i) - T_inf); # Última fila


for i=2:N - 1
    F(N * i, 1) = a * ((x(N * i - 1) - 2 * x(N * i)) / (dx) ^ 2 + (x(N * i - N) - 2 * x(N * i) + x(N * i + N)) / (
    dx) ^ 2); % Columna de la derecha


for i=1:N - 1
    F(N * i + 1, 1) = -(m_a * ((x(N * i + 1)) - x(N * i + 1 - N)) / (dy)) - (
            (a_esp * h_agua) * 1000 / (ro_s * Cp_s) * (x(N * i + 1) - x(N * i + 2))); # Columna de la izquierda(Acá va la ecuacion del serpentin - )


for i=1

    F(i, 1) = 0


# CAMBIO DE LA TEMPERATURA EN LA PLACA