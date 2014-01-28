import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


xf=1000
omega=np.linspace(0,xf,500)

K,E0,tau,om0 = 1,1,1,0.01

fig, (plt1, plt2) = plt.subplots(nrows=2, sharex=True)

plt1.plot(omega,20.*np.log(K)-10*np.log(1+tau*tau*omega*omega),
            label="$Adb(\omega)$",linewidth=3)

plt2.plot(omega,-np.arctan(tau*omega),
            label="$\varphi(\omega)$",linewidth=3)


plt1.grid(True, which="both", linestyle="dotted")
plt2.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
plt1.legend(loc='upper right', fancybox=True, shadow=True, prop=dict(size=10))
#plt2.legend(loc='upper right', fancybox=True, shadow=True, prop=dict(size=10))
#plt.xlabel("$\omega$ $rad/s$")
#plt.xlabel("$\omega$ $rad/s$")

#plt.ylabel("Position $y(t)$ en $m$")
#plt.axis([0,xf,-1.5,1.5])
plt.show()


