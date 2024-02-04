import pandas as pd
import numpy as np

#read data from ods
all_data = pd.read_excel('/home/freeman/Desktop/lab1.ods')
temp_of_thermostat = all_data['T, C^o'].dropna().to_numpy()
delta_pressure = all_data['delta P, bar'].to_numpy()
delta_temp = all_data['delta t, C^o'].to_numpy()

import matplotlib.pyplot as plt

#create plot
delta_pressure=delta_pressure[1:6]
delta_pressure=np.append(delta_pressure, 0) # add (0,0)
delta_temp_at_temp_1=delta_temp[1:6]
delta_temp_at_temp_1=np.append(delta_temp_at_temp_1, 0) # add (0,0) 
delta_temp_at_temp_2=delta_temp[6:11]
delta_temp_at_temp_2=np.append(delta_temp_at_temp_2, 0) # add (0,0)
delta_temp_at_temp_3=delta_temp[11:16]
delta_temp_at_temp_3=np.append(delta_temp_at_temp_3, 0) # add (0,0)

fig, axes = plt.subplots()

axes.plot(delta_pressure, delta_temp_at_temp_1, 'r')
#axes.scatter(delta_pressure, delta_temp_at_temp_1, 'r')
axes.plot(delta_pressure, delta_temp_at_temp_2, 'g')
#axes.scatter(delta_pressure, delta_temp_at_temp_2, 'g')
axes.plot(delta_pressure, delta_temp_at_temp_3, 'b')
#axes.scatter(delta_pressure, delta_temp_at_temp_3, 'b')

axes.set_xlabel('delta_pressure, bar')
axes.set_ylabel('delta_temp, C^o')
axes.set_title('delta_temp versus delta_pressure plot');

plt.show()

#plt.figure()

#plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

#plt.xlabel(r'delta_pressure, bar')
#plt.ylabel(r'delta_temp, C^o')

#plt.grid()
#plt.legend(loc='best')

#plt.show()
