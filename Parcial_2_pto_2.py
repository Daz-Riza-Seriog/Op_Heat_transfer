# Code made for Sergio Andres Diaz Ariza
# 25 November 2021
# License MIT
# Heat Operations: Python Program

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

########### PUNTO 2 ##########
### Punto A ####
#Aire
V_air = 25 # [m/s]
D_ext = 0.1+ (0.05/1000)
miu_cin_air = 1.918e-5
k_air = 0.02662 # [W/m*K]
Re_air = (V_air*D_ext)/miu_cin_air
C_air = 0.027
m_air = 0.805
Pr_air = 0.7255

Nu_air = C_air*(Re_air**m_air)*(Pr_air**(1/3))
h_air = Nu_air*k_air/D_ext

# Agua
D_in = 0.1 #[m]
m_dot = 1 #[Kg/s]
miu_din_agua = 0.653e-3 #[Kg/m*S]
rho_agua = 992.1 #[Kg/m^3]
Cp_agua = 4179 #[J/Kg*K]
miu_cin_agua = miu_din_agua/rho_agua
k_agua = 0.631 #[W/m*K]

Re_agua = (4*m_dot)/(np.pi*D_in*miu_din_agua)
Nu_agua = 0.023*(Re_agua**(4/5))*(Pr_air ** 0.3)
h_agua = (Nu_agua*k_agua)/D_in
print(h_agua)

k_stain = 15.1 #[@W/m*K]

R_agua = 1/h_agua
R_stain = ((D_in/2)/k_stain)*np.log((D_ext/2)/(D_in/2))
R_air = ((D_in/2)/(D_ext/2))*(1/h_air)

U = 1/(R_agua+R_stain+R_air)

T_inf = 37.8+273.15 #[K]
T_i = 40+273.15 #[K]
P = 2*np.pi*(D_in/2)


x_ = np.linspace(0,0.8, endpoint=True)
T_m = T_inf-(T_inf-T_i)*np.exp(-(U*x_*P)/(m_dot*Cp_agua))

### Punto B ####
T_o = T_inf-(T_inf-T_i)*np.exp(-(U*0.8*P)/(m_dot*Cp_agua))

### Punto C ###
A_s = P*0.8
Delta_T_lm = ((T_inf-T_o)-(T_inf-T_i))/(np.log(((T_inf-T_i)/(T_inf-T_o))))
q_tot = U*A_s*Delta_T_lm
print(Delta_T_lm)

print(q_tot)



plt.figure(1)
plt.plot(x_,T_m,'b')
plt.xlabel("Longitud $[m]$")
plt.ylabel("Temperatura $[K]$")
plt.show()

