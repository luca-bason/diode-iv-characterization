from numpy import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T=298.46 #Temperature in Kelvin
q=1.602176634e-19  #Carica elementare in Coulomb

# Modello teorico da adattare ai dati
def func(x, a, b):
    return a*(exp(b*x/T)-1)


x=array([]); y=array([]); ey=array([])

for line in open("out2.dat"):
    dt=line.split()
    if len(dt)!=3:
        continue
    x=append(x,float(dt[0]))
    y=append(y,float(dt[1]))
    ey=append(ey,float(dt[2]))


# Fit dei dati
guess=[1e-12,10000]
parameters, covariance =curve_fit(func,x,y,sigma=ey,absolute_sigma=True,p0=guess)

a,b=parameters
ea,eb=sqrt(diag(covariance))

print(f"a = {a:.6e} ± {ea:.6e}")
print(f"b = {b:.6e} ± {eb:.6e}")


# Calcolo del chi2
chi2=0
for i in range(0,len(x)):
    chi2 += ((y[i]-func(x[i],a,b))/ey[i])**2

rchi2=chi2/(len(x)-len(parameters))

print(f"chi^2 = {chi2:.3f}")
print(f"reduced chi^2 = {rchi2:.3f}")


#Calcolo della costante di Boltzmann
k_B=q/b
k_B_error=q*eb/b**2

print("k_B teorica = 1.380649e-23 J/K")
print(f"k_B sperimentale = {k_B:.6e} ± {k_B_error:.6e} J/K")


# Plot del fit
v_axis=linspace(x.min(), x.max(), 500)
i_curve=func(v_axis,a,b)

plt.errorbar(x,y,yerr=ey,fmt=".",capsize=3,label="Experimental data")
plt.plot(v_axis,i_curve,label="Diode fit")

plt.xlabel("Voltage [V]")
plt.ylabel("Current [A]")
plt.legend()
plt.tight_layout()

plt.show()