# -*- coding: utf-8 -*-
"""Tarea_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zWnlDFVNS9UkQ9mCQwPC7u-tTaHEVeox
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

#datos 
Lm=0.05 #Longitud en x
Ln=0.05 #Longitud en y

#Condiciones de frontera
Ts=29
Td=25
Tz=25
Tn=25

#discretizar
Nm=6
dm=Lm/(Nm-1)
m=np.linspace(0,Lm,Nm)
Nn=6
dn=Ln/(Nn-1)
n=np.linspace(0,Ln,Nn)

mmesh,nmesh=np.meshgrid(m,n,indexing='ij')

plt.scatter(mmesh,nmesh)


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

h=10
Tinf=4
Kc=0.09
Km=0.20
Lx=0.04
Ly=0.04
dx=1

#Discretizar
N=10   #Nodos en x
M=10   #Nodos en y
x=np.linspace(0,Lx,N)
y=np.linspace(0,Ly,M)

#dx=Lx/(N-1)
#dy=Ly/(M-1)

xmesh,ymesh=np.meshgrid(x,y)

p=1

T=np.zeros((M,N))

for i in range(0,N):
  for j in range(0,M):
    T[i][j]=30

#Esquina superior-derecha
T[0][N-1]=(2*T[1][N-1]+T[0][N-2]+h*dx/Kc*Tinf)/((h*dx)/Kc+3)

#Superficie inferior
for i in range(0,N):
  T[M-1][i]=4

#Frontera izquierda
for i in range(1,M-1):
  T[i][0]=(T[i-1][0]+2*T[i][1]+T[i+1][0]+2*h*dx*Tinf/Km)/((2*h*dx/Km)+4)

#Frontera superior
for i in range(1,N-1):
  T[0][i]=(T[0][i+1]+T[1][i]+T[0][i-1]+2*h*dx*Tinf/Kc)/((2*h*dx/Kc)+4)

#Esquina superior-izquierda
T[0][0]=(Kc*T[0][1]+Km*T[1][0]+2*h*dx*Tinf)/(2*h*dx+Kc+Km)

while p>=0:
  #Frontera derecha
  for i in range(1,M-1):
    T[i][N-1]=(T[i-1][N-1]+2*T[i][N-2]+T[i+1][N-1])/4

  #Nodos internos
  for i in range(1,M-1):
    for j in range(1,N-1):
      #chocolate
      if i<j:
        T[i][j]=(T[i][j+1]+T[i+1][j]+T[i][j-1]+T[i-1][j])/4
      #molde
      elif i>j:
        T[i][j]=(T[i][j+1]+T[i+1][j]+T[i][j-1]+T[i-1][j])/4

  #Interfase
  for i in range(1,M-1):
    T[i][i]=(Kc*(T[i][i+1]+T[i-1][i])+Km*(T[i][i-1]+T[i+1][i]))/(2*(Kc+Km))
  
  p-=1

#print(T)

sns.heatmap(T)