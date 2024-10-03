import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve

def s(x):
    return -1.6 * x ** 2 + 1.3 * x + 141.3
def r(x):
    return 1.4 * x ** 2 - 5.6 * x + 12.6

def inter(x):
    return s(x) - r(x)

x = np.linspace(0,10)

sol = np.unique(np.round(fsolve(inter,x),2))
print(sol)


def D(t):
    return (50 * math.e ** (0.3 * t)) - 551

t = np.linspace(0,12,1)
sol = fsolve(D,t)
print(sol[0])

def D(t):
    return (50 * math.e ** (0.3 * t))
print(np.round(D(6),1))


def M(x):
    return x ** 3 - 4 * x ** 2 + 5 * x

print(np.round(M(10)))

def C(n):
    return 50 * n + 200 - 1500

n = np.linspace(0,10,1)

sol = fsolve(C,n)

print(sol[0])

def C(n):
    return 50 * n + 200

print(C(20))

def S(n):
    return 2 * n ** 2 + 3 * n + 5 - 500

n = np.linspace(0,10,1)

sol = fsolve(S,n)

print(sol)

def S(n):
    return 2 * n ** 2 + 3 * n + 5
print(S(50))


horas_capacitacion = np.array([5,10,15,20])
productividad = np.array([50,80,110,140])

pendiente,inter = np.polyfit(horas_capacitacion,productividad,1)
print(pendiente,np.round(inter))

def f(x):
    return pendiente * x + inter

print(f(5))

def I(x):
    return 50 * x + 0.5 * x ** 2

def C(x):
    return 10 * x + 450

def inter(x):
    return I(x) - C(x)

x = np.linspace(0,10,1)

sol = np.unique(fsolve(inter,x))
print(sol,C(10),I(10))