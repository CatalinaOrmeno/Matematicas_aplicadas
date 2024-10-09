import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve

a1 = 0
d = 0
def A(n):
    return a1 + (n - 1) * d
'''
a1 = 12000
d = 2000

resultados = [A(n) for n in range(25)]

print(resultados[14])
print(sum(resultados))
'''
'''
a1 = 3
d = -0.1
resultados = [A(n) for n in range(11)]
#A)
print(resultados[5])
#B)
print(sum(resultados))
'''
'''
#A) El primer termino de la suceción es 56 = A1
#B) An = -56 +(n - 1)* 4
a1 = -56
d = 4
#C)
resultados = [A(n) for n in range(436)]
print(resultados[100])
#D) Se supone que deberia ser la pocisión 435
print(resultados[435])
'''