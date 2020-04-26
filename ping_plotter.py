import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

def parser():
    with open('ping_logs.txt') as logger:
        data =logger.readlines()

    timehistory = []
    pinghistory = []
    for line in data:
        if len(line) != 0:
            log_time, ping = line.split('->')
            ping = ping.replace('ms\n','')
            ping = int(ping)
            log_datetime = datetime.strptime(log_time, "%Y-%m-%d %H:%M:%S")
            #print(log_datetime, ping)
            timehistory.append(log_datetime)
            pinghistory.append(ping)
    return timehistory, pinghistory


timehistory, pinghistory = parser()

# plt.plot(timehistory, pinghistory)
# plt.xlabel('Date time')
# plt.ylabel('Ping (ms)')
# plt.show()

#style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    timehistory, pinghistory = parser()
    ax1.clear()
    ax1.plot(timehistory, pinghistory)

ani = animation.FuncAnimation(fig, animate, interval=6000)
plt.show()
