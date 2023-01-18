import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure(figsize=(15,9))
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data1 = open('data/tx-133','r').read()
    graph_data2 = open('data/tx-132','r').read()
    graph_data3 = open('data/tx-134','r').read()

    lines1 = graph_data1.split('\n')
    lines2 = graph_data2.split('\n')
    lines3 = graph_data3.split('\n')
    xs1 = []
    ys1 = []
    xs2 = []
    ys2 = []
    xs3 = []
    ys3 = []

    times = 0
    for line in lines1:
        if len(line) > 1:
            xs1.append(float(times))
            ys1.append(float(line)/1000)
        times = times + 1

    times = 0
    for line in lines2:
        if len(line) > 1:
            xs2.append(float(times))
            ys2.append(float(line)/1000)
        times = times + 1
    times = 0
    for line in lines3:
        if len(line) > 1:
            xs3.append(float(times))
            ys3.append(float(line)/1000)
        times = times + 1
    
    ax1.clear()
    #plt.yscale("log", basey=2)
    ax1.set_ylim([0,12])
    ax1.plot(xs1, ys1,color='red',label='Sliced TCP')
    ax1.plot(xs2, ys2,color='blue',label='Non Sliced TCP')
    ax1.plot(xs3, ys3,color='green',label='background')
    plt.xticks(size=25)
    plt.yticks(size=25)
    ax1.legend(loc='upper left', shadow=True, prop={'size':25}) 
    ax1.set_xlabel('Time (s)',size=25)
    ax1.set_ylabel('Bandwidth (Gbit/s)',size=25)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
