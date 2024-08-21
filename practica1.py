import matplotlib.pyplot as plt
import numpy as np

def banco_estado(t):
    return 10000*(1+0.0511)**t

def mercado_pago(t):
    return 10000*(1+0.054)**t

#Dominio contextualizado: [0,12]
tiempo = np.arange(0,13)
banco1 = banco_estado(tiempo)
banco2 = mercado_pago(tiempo)
plt.plot(tiempo,banco1,label='Banco Estado')
plt.plot(tiempo,banco2,label='Mercado Pago')
print(banco1)
for ind,elem in enumerate(banco1):
    if elem == 156601.64682302:
        plt.scatter(ind,banco1[ind],label='$150.000')
plt.axis([0,12,10000,max(banco2)])

plt.title('Comparacion de ganacias en intereses de bancos según el tiempo transcurrido')
plt.xlabel('Cantidad de tiempo(meses)')
plt.ylabel('Cantidad de intereses acumulados')
plt.grid(True)
plt.legend()
plt.show()