# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
import math

import time

N = 100  # número total de individuos
p_infectado = 0.05  # probabilidad de que un individio generado sea infectado

p_medico = 0.05  # probabilidad de que un individio generado sea médico

R = 2.0  # radio de infección
I = 0.5  # probabilidad de infección
v = 3  # velocidad máxima de los individuos
T = 100  # tamaño (cuadrado T*T)

# 0 = posición x (0-T)
# 1 = posición y (0-T)
# 2 = velocidad (1,v)
# 3 = dirección (0,359)
# 4 = estado - 0: normal 1: infectado 2: médico


"""
PENDIENTE

- Separar en funciones
- Infectar/curar. La función de infección solo está activa en los infectados/curados
- Cada x frames que aparezca un médico
- Rebotar bien (simétrico respecto de la normal). Mirar que no se salgan del tablero
- Arreglar movimiento (ahora tiene valores decimales por los cosenos y eso y tiene que ser entero)
- Evitar for. Por ejemplo al establecer valores iniciales sustituir por el vector con los números random directamente
- Hacer el tablero cuadrado
- Comprobar que los colores corresponden con los estados (por el cmap)


"""


A = np.zeros([N, 5])

filas, columnas = np.shape(A)

for i in range(filas):

    A[i, 0] = np.random.randint(0, T)

    A[i, 1] = np.random.randint(0, T)

    A[i, 2] = np.random.randint(1, v)

    A[i, 3] = np.random.randint(0, 359)

    A[i, 4] = random.choices(
        [0, 1, 2], weights=[1-p_infectado-p_medico, p_infectado, p_medico])[0]

numeropi = math.pi

while True:
    for j in range(N):

        if A[j, 0] < 0 or A[j, 0] > T or A[j, 1] < 0 or A[j, 1] > T:

            A[j, 2] = A[j, 2] * (-1)

        A[j, 0] += round(A[j, 2]*math.cos((A[j, 3]*numeropi)/180))
        A[j, 1] += round(A[j, 2]*math.sin((A[j, 3]*numeropi)/180))

        """ Esto es para que aparezca en el otro extremo de la pantalla
            habria que poner abs(T-posición) o algo asi
        
            A[j, 0] = A[j, 0] * (-1)
            A[j, 1] = A[j, 1] * (-1)
        """

    x = A[:, 0]
    y = A[:, 1]
    estado = A[:, 4]

    plt.scatter(x, y, c=estado, cmap="brg")

    plt.xlim([0, T])
    plt.ylim([0, T])
    plt.show()

    time.sleep(0.02)

"""
pos = T * np.random.rand(N, 2)

vel = v * (2 * np.random.rand(N, 2) - 1)

status = np.zeros(N, dtype=int)

infected = np.random.choice(N, size=int(p*N), replace=False)
status[infected] = 1

def update_pos(pos, vel):
    pos += vel
    pos[pos > L] -= L
    pos[pos < 0] += L
    return pos

def update_status(pos, status):
    for i in range(N):
        if status[i] == 1:
            dist = np.sqrt(np.sum((pos - pos[i])**2, axis=1))
            j = np.where(dist < R)[0]
            for k in j:
                if status[k] == 0:
                    if np.random.rand() < I:
                        status[k] = 1
    return status

def animate(i):
    global pos, vel, status
    pos = update_pos(pos, vel)
    status = update_status(pos, status)
    plt.clf()
    plt.plot(pos[status==0,0], pos[status==0,1], 'bo')
    plt.plot(pos[status==1,0], pos[status==1,1], 'ro')
    plt.xlim([0, L])
    plt.ylim([0, L])
    plt.title('Iteración {}'.format(i))
    return plt.gcf()

fig = plt.figure(figsize=(6, 6))
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
"""
