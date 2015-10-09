#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

def Lorenz(t,v,cons):
#funcion para definir las ecuaciones de lorenz, t=tiempo, v=variables (x,y,z)

  sigma=cons[0]
  beta=cons[1]
  rho=cons[2]

  dv=np.zeros([3])
  dv[0]=sigma*(v[2]-v[1]) #dx/ds
  dv[1]=v[0]*(rho-v[2])-v[1] #dy/ds
  dv[2]=v[0]*v[1]-beta*v[2] #dz/ds


  return dv


cons=[10 , 2.666 , 28]
ti=0 #tiempo inicial
tf=200 #tiempo final
dt=0.001 #paso de tiempo
vi=[100,2000,400] #condiciones iniciales
s=[]
t=[]

solucion = ode(Lorenz).set_integrator('vode',method='adams')
#solucion por metodo runge-kutta de orden 4
#solucion.set_initial_value(vi,ti)
solucion.set_f_params(cons).set_initial_value(vi,ti) #incluye parametros dentro de la solucion

while solucion.successful() and solucion.t+dt < tf:
  '''
  la iteracion sigue mientras el metodo runge-kutta funcione y no se llegue
  al tiempo final
  '''
  solucion.integrate(solucion.t+dt) #integra desde ti hasta tf avanzando dt
  s.append(solucion.y)
  t.append(solucion.t)

s= np.array(s)
print s

fig = plt.figure(3)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.set_title(r'$Grafico \ de \ las \ soluciones \ de \ las \ ecuasiones \ de \ Lorenz$')
ax.plot(s[:,0], s[:,1],s[:,2],'r-') #plot(x,y,z)
ax.set_xlabel(r'$Eje \ X$')
ax.set_ylabel(r'$Eje \ Y$')
ax.set_zlabel(r'$Eje \ Z$')
fig.savefig('3d')
plt.show()
