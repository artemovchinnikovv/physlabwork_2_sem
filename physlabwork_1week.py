import pandas as pd
import numpy as np

#read data from ods
all_data = pd.read_excel('/home/freeman/Desktop/physlabwork_1week.ods')
temp_of_thermostat = all_data['T, C^o'].dropna().to_numpy()
delta_pressure = all_data['delta P, bar'].to_numpy()
delta_temp = all_data['delta t, C^o'].to_numpy()

import matplotlib.pyplot as plt

#create massives
delta_pressure=delta_pressure[1:6]
delta_pressure=np.append(delta_pressure, 0) # add (0,0)
delta_temp_at_temp_1=delta_temp[1:6]
delta_temp_at_temp_1=np.append(delta_temp_at_temp_1, 0) # add (0,0) 
delta_temp_at_temp_2=delta_temp[6:11]
delta_temp_at_temp_2=np.append(delta_temp_at_temp_2, 0) # add (0,0)
delta_temp_at_temp_3=delta_temp[11:16]
delta_temp_at_temp_3=np.append(delta_temp_at_temp_3, 0) # add (0,0)

#figure
fig, axes = plt.subplots()

#plot
axes.plot(delta_pressure, delta_temp_at_temp_1, 'red')
axes.scatter(delta_pressure, delta_temp_at_temp_1, c='red', linewidths=0)
axes.plot(delta_pressure, delta_temp_at_temp_2, 'green')
axes.scatter(delta_pressure, delta_temp_at_temp_2, c='green', linewidth=0)
axes.plot(delta_pressure, delta_temp_at_temp_3, 'blue')
axes.scatter(delta_pressure, delta_temp_at_temp_3, c='blue', linewidth=0)

from scipy.optimize import curve_fit

#fit
def func(x, a, b):
	return a*x+b
popt_1, pcov_1 = curve_fit(func, delta_pressure, delta_temp_at_temp_1)
popt_2, pcov_2 = curve_fit(func, delta_pressure, delta_temp_at_temp_2)
popt_3, pcov_3 = curve_fit(func, delta_pressure, delta_temp_at_temp_3)

#additional
axes.set_xlabel('delta_pressure, bar')
axes.set_ylabel('delta_temp, C^o')
axes.set_title('delta_temp versus delta_pressure plot');
text_1='y = '+str(round (popt_1[0], 2))+' * x + '+str(round (popt_1[1], 2))
text_2='y = '+str(round (popt_2[0], 2))+' * x + '+str(round (popt_2[1], 2))
text_3='y = '+str(round (popt_3[0], 2))+' * x + '+str(round (popt_3[1], 2))
axes.legend(['temp_of_thermostat = 18 C^o', text_1, 'temp_of_thermostat = 30 C^o', text_2, 'temp_of_thermostat = 50 C^o', text_3])

#fit plots
axes.plot(delta_pressure, func(delta_pressure, popt_1[0], popt_1[1]), 'r--')
axes.plot(delta_pressure, func(delta_pressure, popt_2[0], popt_2[1]), 'g--')
axes.plot(delta_pressure, func(delta_pressure, popt_3[0], popt_3[1]), 'b--')

#errorbar
axes.errorbar(delta_pressure, delta_temp_at_temp_1, xerr=0.05, yerr=0.019, color='red',ecolor='black')
axes.errorbar(delta_pressure, delta_temp_at_temp_2, xerr=0.05, yerr=0.019, color='green',ecolor='black')
axes.errorbar(delta_pressure, delta_temp_at_temp_3, xerr=0.05, yerr=0.019, color='blue',ecolor='black')

#show
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
