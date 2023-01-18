import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure(figsize=(15,9))
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data1 = open('data/tx- 16','r').read()
    # graph_data2 = open('data/tx-','r').read()

    lines1 = graph_data1.split('\n')
    # lines2 = graph_data2.split('\n')
    xs1 = []
    ys1 = []
    # xs2 = []
    # ys2 = []

    times = 0
    for line in lines1:
        if len(line) > 1:
            xs1.append(float(times))
            ys1.append(float(line)/1000)
        times = times + 1

      
    # for line in lines2:
    #     if len(line) > 1:
    #         y,x=line.split(' ')
    #         if(y!=""):
    #             xs2.append(float(x))
    #             ys2.append(float(y)/1000000000)
    
    ax1.clear()
    ax1.set_ylim([0,12])
    ax1.plot(xs1, ys1,color='blue',label='free5GC UPF')
    plt.xticks(size=25)
    plt.yticks(size=25)
    # ax1.plot(xs2, ys2,color='blue',label='background')
    ax1.legend(loc='right', shadow=True, prop={'size':25}) 
    ax1.set_xlabel('Time (s)',size=25)
    ax1.set_ylabel('Bandwidth (Gbit/s)',size=25)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
