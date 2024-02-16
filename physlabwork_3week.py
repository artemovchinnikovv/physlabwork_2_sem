import pandas as pd
import numpy as np

#read data from ods
all_data = pd.read_excel('physlabwork_3week.ods')

x_1_div_temp_K = all_data['1/(temperature, K)'].dropna().to_numpy()
y_ln_delta_pressure_Pa = all_data['LN (delta_pressure, Pa)'].dropna().to_numpy()

import matplotlib.pyplot as plt

#figure
fig, axes = plt.subplots()

#plot
axes.plot(x_1_div_temp_K, y_ln_delta_pressure_Pa, 'red')

from scipy.optimize import curve_fit

#fit
def func(x, a, b):
	return a*x+b
popt, pcov = curve_fit(func, x_1_div_temp_K, y_ln_delta_pressure_Pa)
print (popt)
print (pcov)

#grid
plt.grid()

#fit plots
axes.plot(x_1_div_temp_K, func(x_1_div_temp_K, popt[0], popt[1]), 'b--')

#additional
axes.set_xlabel('x_1_div_temp_K')
axes.set_ylabel('y_ln_delta_pressure_Pa')
axes.set_title('x_1_div_temp_K vs y_ln_delta_pressure_Pa plot');
text='least squares fitting line, y = '+str(round (popt[0], 2))+' * x + '+str(round (popt[1], 2))
axes.legend(['experimental data (alcohol)', text])

#errorbar
axes.errorbar(x_1_div_temp_K, y_ln_delta_pressure_Pa, xerr=0, yerr=0, color='red',ecolor='black')

#scatter
axes.scatter(x_1_div_temp_K, y_ln_delta_pressure_Pa, c='red', linewidths=0)

#show
#plt.show()

#save
plt.savefig('physlabwork_3week_plot.svg')

#plt.figure()

#plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

#plt.xlabel(r'delta_pressure, bar')
#plt.ylabel(r'delta_temp, C^o')

#plt.grid()
#plt.legend(loc='best')

#plt.show()
