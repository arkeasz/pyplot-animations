import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.linspace(0, 3, 40)
G = -9.81

v0 = 12
z = v0*t + 1/2*G*t**2
# x = v0*t
# print()


# line2 = ax.plot(t, z, label=f'v0 = {v0} m/s')[0]
line2 = ax.plot(t[0], z[0], label=f'v0 = {v0} m/s')[0]

# ball
# ball_radius = .1
# ball = plt.Circle((t[0], z[0]), ball_radius, fc="blue")

# ax.add_patch(ball)
# f: frames
def update(f):
#     # x = t[:f]
#     # y = z[:f]
    line2.set_xdata(t[:f])
    line2.set_ydata(z[:f])
    # ball.set_center((t[f-1], z[f-1]))
    # ball.set_center((t[f-1], z[f-1]))
    return line2


ax.legend()
ax.set(xlim=[0, 3], ylim=[-4, 10], ylabel="z(m)", xlabel= "t(s)", )
# ax.set_aspect('equal', adjustable='box')
ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
ani.save(filename="./movimiento_parabolico.gif", writer="pillow")

plt.show()
