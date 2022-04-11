#use the anitmate function of matplotlib to create a live plot of bitcoin_price66.csv.
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open("price66.csv", "r").read()
    lines = graph_data.split("\n")
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(y)
            ys.append(x)
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()