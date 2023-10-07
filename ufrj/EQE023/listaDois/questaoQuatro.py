import numpy as np
from scipy import interpolate

Ts = 423.15  # K
Tinf = 268.15  # K
Tf = (Ts + Tinf) / 2.0  # K

# arrays para interpolação das propriedades termofísicas
T = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
rho = np.array([2.3364, 1.7458, 1.3947, 1.1614, 0.9950, 0.8711, 0.7740, 0.6964, 0.6329, 0.5804])
# os valores na tabela de cp devem ser multiplicados por 1000 para converter as unidades
cp = np.array([1012, 1007, 1006, 1007, 1009, 1014, 1021, 1030, 1040, 1051])
# os valores na tabela de mi já estão multiplicados por 10^7 logo devem ser divididos por 10^7
mi = np.array([103.4e-7, 132.5e-7, 169.6e-7, 184.6e-7, 208.2e-7, 230.11e-7, 250.7e-7, 270.1e-7, 288.4e-7, 305.8e-7])
# os valores na tabela de k já estão multiplicados por 10^3 logo devem ser divididos por 10^3
k = np.array([13.8e-3, 18.1e-3, 22.3e-3, 26.3e-3, 30.0e-3, 33.8e-3, 37.3e-3, 40.7e-3, 43.9e-3, 46.9e-3])

rho_int = interpolate.interp1d(T, rho)
cp_int = interpolate.interp1d(T, cp)
mi_int = interpolate.interp1d(T, mi)
k_int = interpolate.interp1d(T, k)

# propriedades em Ts
rho_ts = rho_int(Ts)
cp_ts = cp_int(Ts)
mi_ts = mi_int(Ts)
k_ts = k_int(Ts)
# propriedades em Tinf
rho_tinf = rho_int(Tinf)
cp_tinf = cp_int(Tinf)
mi_tinf = mi_int(Tinf)
k_tinf = k_int(Tinf)
# propriedades em Tf
rho_tf = rho_int(Tf)
cp_tf = cp_int(Tf)
mi_tf = mi_int(Tf)
k_tf = k_int(Tf)

D = 0.5  # m
As = np.pi * D  # m²
vinf = 5.0  # m/s

# Número de Prandtl (Pr)
def prandtl(Cp, mi, k):
    return (Cp * mi) / k
# onde:
# Cp é a capacidade calorífica do fluido (J/kg.K)
# k é a condutividade térmica do fluido (W/m.K)

# Número de Reynolds (Red)
def reynolds(rho, mi):
    return (rho * vinf * D) / mi
# onde:
# rho (ρ) é massa específica do fluido (kg/m³)
# vinf (v∞) é velocidade de escoamento sobre o cilindro (m/s)
# mi (μ) é viscosidade dinâmica do fluido (N.s/m²)


# Nº de Prandtl em cada temperatura
pr_ts = prandtl(cp_ts, mi_ts, k_ts)
pr_tinf = prandtl(cp_tinf, mi_tinf, k_tinf)
pr_tf = prandtl(cp_tf, mi_tf, k_tf)

# Nº de Reynolds em cada temperatura
red_ts = reynolds(rho_ts, mi_ts)
red_tinf = reynolds(rho_tinf, mi_tinf)
red_tf = reynolds(rho_tf, mi_tf)

# print(pr_tf)
# print(pr_ts)
# print(pr_tinf)
# print(red_tf * pr_tf)
# Através dos prints, descobrimos que:
# red_tf * pr_tf é maior que 0.2
# pr_ts é aproximadamente igual a 0.7
# pr_tinf menor do que 10, logo n = 0,37

n = 0.37

# print(red_ts)
# print(red_tinf)
# Através dos prints, descobrimos que:
# red_ts está entre 40 000 e 400 000
# red_tinf está entre 1000 e 2e5


# I) Correlação de Hilpert
def h_hilpert(k, Red, Pr):
    C = 0.027
    m = 0.805
    return k * C * (Red * m) * (Pr * 1 / 3) / D

# II) Correlação de Zukauskas
def h_zukauskas(k, Red, Pr):
    C = 0.26
    m = 0.6
    return k*C*(Red*m)(Pr*n)((Pr/pr_ts)**1/4) / D

# III) Correlação de Churchill
def h_churchill(k, Red, Pr):
    return (k/D) * (0.3 + (0.62*(Red*1/2)(Pr*1/3) / (1 + (0.4/Pr)2/3)1/4) * (1 + (Red / 282e3)5/8)*4/5)


def qprima(h):
    return h*As*(Ts-Tinf)

hh = h_hilpert(k_ts, red_ts, pr_ts)
hz = h_zukauskas(k_tinf, red_tinf, pr_tinf)
hc = h_churchill(k_tf, red_tf, pr_tf)

print("Taxa de calor perdido partindo da correlação de Hilpert: ", qprima(hh), "W/m")
print("Taxa de calor perdido partindo da correlação de Zukauskas: ", qprima(hz), "W/m")
print("Taxa de calor perdido partindo da correlação de Churchill: ", qprima(hc), "W/m")
