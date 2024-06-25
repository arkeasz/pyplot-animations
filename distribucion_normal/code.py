import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-5,5,120)

def dist(sigma, mu, x):
    eq = (1/(sigma*np.sqrt(2*np.pi)))*np.exp((-(x-mu)**2)/(2*sigma**2))
    return eq

line1, = ax.plot([], [], "s--b", label=f"lin1")
line2, = ax.plot([], [], ".m", label=f"lin2")
line3, = ax.plot([], [], "--", label=f"lin3")
line4, = ax.plot([], [], "*", label=f"lin4")

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])

def update(f):
    line1.set_data(x[:f], dist(np.sqrt(0.2), 0, x[:f]))
    line2.set_data(x[:f], dist(np.sqrt(1), 0, x[:f]))
    line3.set_data(x[:f], dist(np.sqrt(5), 0, x[:f]))
    line4.set_data(x[:f], dist(np.sqrt(0.5), -2, x[:f]))

    return (line1, line2, line3, line4)

ax.legend()

ani = animation.FuncAnimation(init_func = init, fig = fig, func = update, frames = len(x), interval = 100)
ani.save(filename="./distribucion_normal.gif", writer="pillow")
plt.axis([-5, 5, 0, 1.])
plt.grid(True)
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("Distribución Normal")
plt.show()
