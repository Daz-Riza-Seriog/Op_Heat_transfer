# Code made for Sergio Andres Diaz Ariza
# 25 November 2021
# License MIT
# Heat Operations: Python Program

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

################## POINT 1 ###################
#### Punto A ####
T_s = 350+273.15 #[K]
T_i = 25+273.15 #[K]
rho_air = 1.184 #[Kg/m^3]
Cp_air = 1007 #[J/Kg*K]



S_t = 24/1000 #[m]
V = 12 #[m/s]
D = 12/1000 #[m]
miu_cin = 1.562e-5 #[m2/s] at 300 K

V_max = S_t*V/(S_t-D)
R_e_max = V_max*D/miu_cin


Pr = 0.7296
Pr_s = 0.6937
C1 = 0.27
m = 0.63
C2 = 0.86
k = 0.02551 #[W/m*K]

Nu_1 = C1*(R_e_max**m)*(Pr**0.36)*((Pr/Pr_s)**(1/4))
Nu_2 = C2*Nu_1


h = Nu_2*k/D
print(h)

x_ = np.linspace(0,3, endpoint=True)
T_m = T_s-(T_s-T_i)*np.exp(-(h*x_*np.pi*D)/(rho_air*V*S_t*Cp_air))


### Punto B ###
T_o = T_s-(T_s-T_i)*np.exp(-(h*3*np.pi*D)/(rho_air*V*S_t*Cp_air))
print(T_o)

rho_air2 = 1.109 #[Kg/m^3]
Cp_air2 = 1007 #[J/Kg*K]
Pr2 = 0.7241
Pr_s = 0.6937
C1 = 0.27
m = 0.63
C2 = 0.86
k2 = 0.02699 #[W/m*K]
miu_cin2 = 1.941e-5

R_e_max2 = V_max*D/miu_cin2

Nu_1_2 = C1*(R_e_max2**m)*(Pr2**0.36)*((Pr2/Pr_s)**(1/4))
Nu_2_2 = C2*Nu_1_2

h2 = Nu_2_2*k2/D
T_o2 = T_s-(T_s-T_i)*np.exp(-(h2*3*np.pi*D)/(rho_air2*V*S_t*Cp_air2))
print(T_o2)

### Punto C ###

Delta_T_lm = ((T_s-T_i)-(T_s-T_o2))/(np.log(((T_s-T_i)/(T_s-T_o2))))
q_flux = 12*h*np.pi*D*Delta_T_lm
q_tot = q_flux*(250/1000)
print(q_tot)



plt.figure(1)
plt.plot(x_,T_m,'r')
plt.xlabel("$N_L$ pasos")
plt.ylabel("Temperatura $[K]$")
plt.show()
