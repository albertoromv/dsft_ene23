import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2,3)

x = np.linspace(0,5,100)
y1 = 3* x + 2
y2 = x**3 + 4

y3 = 3 * (-x) + 2 # con -x es especular en el eje y
y4 = (-x)**3 + 4 # con -x especular en el eje y

y5 = 3*x + 2 - 4 # desplazada 4 unidades a la derecha
y6 = x**3 + 4 - 5 # desplazada 5 unidades a la derecha

ax[0,0].plot(x,y1)
ax[0,1].plot(x,y2)
ax[0,2].plot(x,y3)
ax[1,0].plot(x,y4)
ax[1,1].plot(x,y5)
ax[1,2].plot(x,y6)

ax[0,0].set_title("aquí un título")
ax[1,2].set_title("otro título")
fig.suptitle("Mi figura uno")

plt.tight_layout()

# Otra figura

fig, ax = plt.subplots(2,1)
ax[0].plot(x,y1)
ax[1].plot(x,y2)

fig.suptitle("Mi figura dos")

plt.tight_layout()

print("figuras:", plt.get_fignums())

plt.show()


