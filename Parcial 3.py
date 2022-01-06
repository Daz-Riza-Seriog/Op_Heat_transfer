# Code made for Sergio Andres Diaz Ariza
# 16 December 2021
# License MIT
# Heat Operations: Python Program

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##### Part 1- Masic Flux Oil #####
T_oil_in = 350 + 273.15  # [K]
T_oil_out = 200 + 273.15  # [K]
T_water_in = 170 + 273.15  # [K]
T_water_out = 180 + 273.15  # [K]

# Oil
deltha_T_oil = T_oil_in - T_oil_out
Cp_oil_350 = 3.008  # [KJ/Kg*K]--> 350 Celsisus
Cp_oil_200 = 2.54  # [KJ/Kg*K]--> 200 Celsisus
Cp_oil_prom = (Cp_oil_350 + Cp_oil_200) / 2

# Water
H_vap_water = 2050  # [KJ/Kg]

# Q = m_dot_oil*Cp_oil*(deltha_T_oil) = Q = m_dot_water*H_vap_water

m_dot_water = 0.5  # [Kg/s]
m_dot_oil = (m_dot_water * H_vap_water) / (Cp_oil_prom * deltha_T_oil)

#### Part 2 ####
Q = m_dot_oil * Cp_oil_prom * (deltha_T_oil)
U_sup = 0.350  # [W/m^2*K]

# Cocurrent flow
deltha_T1_co = T_oil_in - T_water_in
deltha_T2_co = T_oil_out - T_water_out

Deltha_T_log_co = (deltha_T1_co - deltha_T2_co) / np.log(deltha_T1_co / deltha_T2_co)

# Counter flow
deltha_T1_con = T_oil_in - T_water_out
deltha_T2_con = T_oil_out - T_water_in

Deltha_T_log_con = (deltha_T1_con - deltha_T2_con) / np.log(deltha_T1_con / deltha_T2_con)

As_co = Q / (U_sup * Deltha_T_log_co)
As_con = Q / (U_sup * Deltha_T_log_con)

# Usamos la de menor Area Superficial por eficiencia
N = 100000  # Suponemos 1000 tubos de Trabajo
D = (As_con / N * 2 * np.pi) * 2
#D = 0.0030610385380016977
D_ext = D+0.002413

miu_cin_oil_prom = 0.995
rho_oil_prom = 700  # [kg/m^3
miu_oil_prom = miu_cin_oil_prom * rho_oil_prom  # [Kg/m*s]

# Calculemos el Reynolds para el Aceite
Re_oil = (4 * m_dot_oil) / (np.pi * D_ext * miu_oil_prom)
Pr_oil = 14.5  # Prom in the exponential range
k_oil = 0.114 #[W/m*K]

# Values of
C_oil = 0.989
m_oil = 0.330
Nu_oil = C_oil * (Re_oil ** m_oil) * (Pr_oil ** (1 / 3))
h_oil = (Nu_oil*k_oil)/D_ext

# Calculemos el Reynolds para el Agua
miu_water_prom = 8.851e-4
Pr_water = 1.05
k_water = 0.3567 #[]w/m*K

Re_water = (4 * m_dot_water) / (np.pi * D * miu_water_prom)
Nu_water = 0.023*(Re_water**4/5)*Pr_water**0.4
h_water = (Nu_water*k_water)/D

# Global coeficient
k_stain = 45 #[@W/m*K]

R_water = 1/h_water
R_stain = ((D/2)/k_stain)*np.log((D_ext/2)/(D/2))
R_oil = ((D/2)/(D_ext/2))*(1/h_oil)

U = 0.01/(R_water+R_stain+R_oil)

As_con_2 = Q / (U * Deltha_T_log_con)
D_2 = (As_con_2 / N * 2 * np.pi) * 2

Q_ideal = (U * Deltha_T_log_con*As_con)

print("Flujo masico de Aceite:", m_dot_oil)
print("Calor Transmitido:", Q)
print("Area superficial Cocorriente:", As_co)
print("Area superficial Contracorriente:", As_con)
print("Diametero de tubos:", D)
print("Reynolds Oil:", Re_oil)
print("Convective coefficient Oil:", h_oil)
print("Reynolds water:", Re_water)
print("Convective coefficient water:", h_water)
print("Coeficiente Global de Transferencia:",U)
print("Area de Transferencia:",As_con_2)
print("Diametero de tubos:", D_2)
print("Diametero de tubos:", Q_ideal)