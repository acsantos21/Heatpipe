import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,100)
y1=np.sin(x)
y2=np.cos(x)

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x, y1, c='r', label='sinx',linewidth=3.0)
ax.plot(x, y2, c='g', label='cosx',linewidth=5.0)

leg = plt.legend()

leg_lines = leg.get_lines()
leg_texts = leg.get_texts()

plt.setp(leg_lines[0], linewidth=6)
plt.setp(leg_lines[1], linewidth=12)
plt.setp(leg_texts, fontsize=10)

plt.show()
