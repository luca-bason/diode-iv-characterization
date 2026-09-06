from ROOT import *
from numpy import *
from ctypes import *

def func(x,a,b):
    return a*(exp(b*x/298.46)-1)

def fcn(npar, gin, f, par,iflag):
    chi2 = 0.0
    for i in range(0,len(x)):
        chi2 += ((y[i]-func(x[i],par[0],par[1]))/ey[i])**2
    f.value = chi2

x=array([]); y=array([]); ey=array([])

for line in open("out2.dat"):
    dt=line.split()
    if len(dt)!=3:
        continue
    x=append(x,float(dt[0]))
    y=append(y,float(dt[1]))
    ey=append(ey,float(dt[2]))

minuit = TMinuit(2)
minuit.SetFCN(fcn)
minuit.DefineParameter(0, 'a',1e-12,1e-14,0., 0.)
minuit.DefineParameter(1, 'b',10000,10.,0., 0.)
minuit.Command("MIGRAD")
a  = c_double(0.0); b  = c_double(0.0)
ea = c_double(0.0); eb = c_double(0.0)
minuit.GetParameter(0,a,ea)
minuit.GetParameter(1,b,eb)

print(f"a = {a.value:.6e} ± {ea.value:.6e}, b = {b.value:.6e} ± {eb.value:.6e}")

q=1.602176634e-19
k_B=q/b
k_B_error=q*eb/b**2

print("k_B teorica = 1.380649e-23 J/K")
print(f"k_B sperimentale = {k_B:.6e} ± {k_B_error:.6e} J/K")
