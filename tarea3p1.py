#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


u_= 1.243 #asignar este valor


def func(y,v):
    return v, -y -u_*(y*y-1)*v



def getk1(y_n,v_n,h,func):
    f_eval= func(y_n,v_n)
    return h*f_eval[0], h*f_eval[1]
    print "k1"
    print getk1[0],getk1[1]


def getk2(y_n,v_n,h,func):
    k1= getk1(y_n,v_n,h,func)
    f_eval= func(y_n + k1[0]/2, v_n + k1[1]/2)
    return h*f_eval[0], h*f_eval[1]
    print "k2"
    print gwtk2[0],getk2[1]



def getk3(y_n,v_n,h,func):
    k1=getk1(y_n,v_n,h,func)
    k2=getk2(y_n,v_n,h,func)
    f_eval=func(y_n-k1[0]-2*k2[0],v_n-k1[0]-2*k2[1])
    return h*f_eval[0], h*f_eval[1]
    print "k3"
    print getk3[0],getk3[1]



def paso_rk3(y_n,v_n,h,func):
    k1=getk1(y_n,v_n,h,func)
    k2=getk2(y_n,v_n,h,func)
    k3=getk3(y_n,v_n,h,func)
    y_n1= y_n + (k1[0]+4*k2[0]+k3[0])/6
    v_n1= v_n + (k1[1]+4*k2[1]+k3[1])/6
    return y_n1,v_n1
    print "paso_rk3"
    print paso_rk3[0],paso_rk3[1]


N_pasos= 1000
h= (20*np.pi)/N_pasos
y=np.zeros(N_pasos)
v=np.zeros(N_pasos)

y[0]=4
v[0]=0

for i in range(1, N_pasos):
    y[i],v[i]= paso_rk3(y[i-1],v[i-1],h,func)


t_rk = [h * i for i in range(N_pasos)]


#plt.figure(1)
#plt.clf()
print y,v

plt.plot(y, v , 'g')




plt.ylabel("$v(t)$")
plt.xlabel('$y(t)$', fontsize=18)
plt.show()
plt.draw()
