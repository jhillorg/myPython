import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('foo.txt', delimiter=',')

print(data)

time = data[:,][:,0]

sensors = data[:,][:,1:3]

print(time)

print(sensors)

avg = np.mean(sensors,1)

print(avg)

# export data
time_col= time.reshape(-1,1)
avg_col= avg.reshape(-1,1)
my_data = np.concatenate((time_col,sensors,avg_col),axis=1)
np.savetxt('foo-analysis.txt', my_data, delimiter=',')

# plot data to PNG file
plt.figure(1)
plt.plot(time,sensors[:,][:,1],'r-')
plt.plot(time,avg,'b-')
plt.legend(['Sensor 2','Average'])
plt.xlabel('Time (sec)')
plt.ylabel('Values')
plt.savefig('foo-analysis.png')
plt.show()
