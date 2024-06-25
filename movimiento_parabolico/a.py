import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.linspace(0,10, 120)
G = -9.81
v0 = 12
theta = np.radians(30)
t = 2*v0*np.sin(theta)/G
y = (v0*np.sin(theta))*t + 1/2*G*t**2
d = v0*np.cos(theta)*t
hmax = v0**2*np.sin(theta)**2/2*G

# line2 = ax.plot(t, z, label=f'v0 = {v0} m/s')[0]

line2 = ax.plot(x[0], y[0], label=f'v0 = {v0} m/s')[0]
# hmax = plt.text(0, h_max, f"altura máxima: {h_max}")

# ball
ball_radius = .1
ball = plt.Circle((x[0], y[0]), ball_radius, fc="blue")
# ax.add_patch(hmax)
ax.add_patch(ball)
# f: frames
def update(f):
#     # x = t[:f]
#     # y = z[:f]
    line2.set_xdata(x[:f])
    line2.set_ydata(y[:f])
    ball.set_center((x[f-1], y[f-1]))
    ball.set_center((x[f-1], y[f-1]))
    return line2, ball


ax.legend()
plt.axis([-1.0, 25.0, -0.5, 8.0])

ax.set(ylabel="z(m)", xlabel= "t(s)", )
# ax.set_aspect('equal', adjustable='box')
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(x), interval=30)
ani.save(filename="./movimiento_parabolico.gif", writer="pillow")

plt.show()
