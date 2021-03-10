import math
import numpy as np
import matplotlib.pyplot as plt


#===============================================================
# === intialisation des variables
#===============================================================

c = 100 * 10**(-6)
E = 5
r = 1000
time = []
t = np.linspace(0,1,1000)
Uc= []
Ur = []

#===============================================================
## ==== charge du condancateur
for i in range(len(t)):
    uc = E * (1 - np.exp((-1 / (r * c)) * t[i]))
    Uc.append(uc)

for i in range(len(t)):
    ur=E*np.exp((-1/(r*c))*t[i])
    Ur.append(ur)
#===============================================================
## ==== décharge du condancateur
for i in range(len(t)):
    uc = E*np.exp((-1/(r*c))*t[i])
    Uc.append(uc)

for i in range(len(t)):
    ur = -(E*np.exp((-1/(r*c))*t[i]))
    Ur.append(ur)

#===============================================================
## ==== charge du condancateur
for i in range(len(t)):
    uc = E * (1 - np.exp((-1 / (r * c)) * t[i]))
    Uc.append(uc)

for i in range(len(t)):
    ur=E*np.exp((-1/(r*c))*t[i])
    Ur.append(ur)
#===============================================================
## ==== décharge du condancateur
for i in range(len(t)):
    uc = E*np.exp((-1/(r*c))*t[i])
    Uc.append(uc)

for i in range(len(t)):
    ur = -(E*np.exp((-1/(r*c))*t[i]))
    Ur.append(ur)

#===============================================================
# == affichage des courbes

fig_r, axs = plt.subplots()
axs.plot(Uc,label='Uc(t)')
axs.plot(Ur,label='Ur(t)')
axs.set_xlabel('Time (s)')
axs.set_title('circuit RC')
axs.legend()
axs.grid(True)

plt.show()