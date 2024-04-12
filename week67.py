import matplotlib.pyplot as plt
import numpy as np

plt.title(r'$I_D-V_D$ curve under different $V_G$ and $Na$')#括号当中输入标题的名称

def Cal_Id(Vg=0, Na=0, Vd=0) -> float:
    '''
        Vg: gate voltage (V)
        Na: doping concentration (cm^(-3))
        Vd: drain voltage (V)
    '''
    epsilon0 = 8.854e-12
    d = 2e-8
    Ci = epsilon0 * 3.9 / d
    un = 0.1
    Z = 1e-4
    L = 5e-6
    kn = un * Z * Ci / L

    ni = 1.5e10
    phiF = 0.026 * np.log(Na / ni)
    Qi = 5e15 * 1.6e-19

    if Na == 1e14:
        phims = -0.82
    elif Na == 1e15:
        phims = -0.9
    elif Na == 1e16:
        phims = -0.96
    elif Na == 1e17:
        phims = -1.04
    
    VFB = phims - Qi / Ci

    Qd = -2 * ((11.8*epsilon0 * 1.6e-19 * Na * 1e6 * phiF) ** 0.5)
    # Here Na needs to be in units of m^(-3)

    VT = VFB - Qd/Ci + 2*phiF

    Id = 0
    if Vg < VT:
        return Id
    else:
        if Vd < (Vg - VT):      # not saturated
            Id = kn * ((Vg-VT)*Vd - 0.5*Vd**2)
        else:                   # saturated
            Vd_sat = Vg - VT
            Id = 0.5 * kn * Vd_sat**2
    return Id

Vd = np.linspace(0, 5, 100)

Na = 1e14
Vg = 1
Id_1_1e14 = []
for vd in Vd:
    Id_1_1e14.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_1_1e14)
plt.plot(Vd, Id_1_1e14, linestyle='-', color='r')

Na = 1e14
Vg = 2
Id_2_1e14 = []
for vd in Vd:
    Id_2_1e14.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_2_1e14)
plt.plot(Vd, Id_2_1e14, linestyle=':', color='r')

Na = 1e14
Vg = 3
Id_3_1e14 = []
for vd in Vd:
    Id_3_1e14.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_3_1e14)
plt.plot(Vd, Id_3_1e14, linestyle='--', color='r')

Na = 1e14
Vg = 4
Id_4_1e14 = []
for vd in Vd:
    Id_4_1e14.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_4_1e14)
plt.plot(Vd, Id_4_1e14, linestyle='-.', color='r')

Na = 1e14
Vg = 5
Id_5_1e14 = []
for vd in Vd:
    Id_5_1e14.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_5_1e14)
plt.plot(Vd, Id_5_1e14, linestyle='-', color='r')

Na = 1e15
Vg = 1
Id_1_1e15 = []
for vd in Vd:
    Id_1_1e15.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_1_1e15)
plt.plot(Vd, Id_1_1e15, linestyle='-', color='b')

Na = 1e15
Vg = 2
Id_2_1e15 = []
for vd in Vd:
    Id_2_1e15.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_2_1e15)
plt.plot(Vd, Id_2_1e15, linestyle=':', color='b')


Na = 1e15
Vg = 3
Id_3_1e15 = []
for vd in Vd:
    Id_3_1e15.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_3_1e15)
plt.plot(Vd, Id_3_1e15, linestyle='--', color='b')


Na = 1e15
Vg = 4
Id_4_1e15 = []
for vd in Vd:
    Id_4_1e15.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_4_1e15)
plt.plot(Vd, Id_4_1e15, linestyle='-.', color='b')


Na = 1e15
Vg = 5
Id_5_1e15 = []
for vd in Vd:
    Id_5_1e15.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_5_1e15)
plt.plot(Vd, Id_5_1e15, linestyle='-', color='b')


Na = 1e16
Vg = 1
Id_1_1e16 = []
for vd in Vd:
    Id_1_1e16.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_1_1e16)
plt.plot(Vd, Id_1_1e16, linestyle='-', color='g')


Na = 1e16
Vg = 2
Id_2_1e16 = []
for vd in Vd:
    Id_2_1e16.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_2_1e16)
plt.plot(Vd, Id_2_1e16, linestyle=':', color='g')


Na = 1e16
Vg = 3
Id_3_1e16 = []
for vd in Vd:
    Id_3_1e16.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_3_1e16)
plt.plot(Vd, Id_3_1e16, linestyle='--', color='g')


Na = 1e16
Vg = 4
Id_4_1e16 = []
for vd in Vd:
    Id_4_1e16.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_4_1e16)
plt.plot(Vd, Id_4_1e16, linestyle='-.', color='g')


Na = 1e16
Vg = 5
Id_5_1e16 = []
for vd in Vd:
    Id_5_1e16.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_5_1e16)
plt.plot(Vd, Id_5_1e16, linestyle='-', color='g')


Na = 1e17
Vg = 1
Id_1_1e17 = []
for vd in Vd:
    Id_1_1e17.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_1_1e17)
plt.plot(Vd, Id_1_1e17, linestyle='-', color='y')


Na = 1e17
Vg = 2
Id_2_1e17 = []
for vd in Vd:
    Id_2_1e17.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_2_1e17)
plt.plot(Vd, Id_2_1e17, linestyle=':', color='y')


Na = 1e17
Vg = 3
Id_3_1e17 = []
for vd in Vd:
    Id_3_1e17.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_3_1e17)
plt.plot(Vd, Id_3_1e17, linestyle='--', color='y')


Na = 1e17
Vg = 4
Id_4_1e17 = []
for vd in Vd:
    Id_4_1e17.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_4_1e17)
plt.plot(Vd, Id_4_1e17, linestyle='-.', color='y')


Na = 1e17
Vg = 5
Id_5_1e17 = []
for vd in Vd:
    Id_5_1e17.append(Cal_Id(Vg, Na, vd))
Id = np.array(Id_5_1e17)
plt.plot(Vd, Id_5_1e17, linestyle='-', color='y')

plt.xlabel(r'$V_D$ (V)')
plt.ylabel(r'$I_D$ (A)')
plt.legend(['Vg=1, Na=1e14', 'Vg=2, Na=1e14', 'Vg=3, Na=1e14', 'Vg=4, Na=1e14', 'Vg=5, Na=1e14',
            'Vg=1, Na=1e15', 'Vg=2, Na=1e15', 'Vg=3, Na=1e15', 'Vg=4, Na=1e15', 'Vg=5, Na=1e15',
            'Vg=1, Na=1e16', 'Vg=2, Na=1e16', 'Vg=3, Na=1e16', 'Vg=4, Na=1e16', 'Vg=5, Na=1e16',
            'Vg=1, Na=1e17', 'Vg=2, Na=1e17', 'Vg=3, Na=1e17', 'Vg=4, Na=1e17', 'Vg=5, Na=1e17'])

plt.show()
