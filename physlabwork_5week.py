import pandas as pd
import numpy as np

#read data from ods
all_data = pd.read_excel('physlabwork_5week.ods')
x_data = all_data['delta P (Pa) (lam)'].dropna().to_numpy()
x_name = "x_delta_press_Pa_lam"
x_error = all_data['error delta P (lam)'].dropna().to_numpy()
y_data = all_data['Q (m3/s) (lam)'].dropna().to_numpy()
y_name = "y_flow_m3_div_s_lam"
y_error = all_data['error Q (lam)'].dropna().to_numpy()

import matplotlib.pyplot as plt

#figure
fig, axes = plt.subplots()

#plot
axes.plot(x_data, y_data, 'red')

from scipy.optimize import curve_fit

#fit
def func(x, a, b):
	return a*x+b
popt, pcov = curve_fit(func, x_data, y_data)
print (popt)
print (pcov)

#grid
plt.grid()

#fit plots
axes.plot(x_data, func(x_data, popt[0], popt[1]), 'b--')

#additional
axes.set_xlabel(x_name)
axes.set_ylabel(y_name)
axes.set_title(x_name + " vs " + y_name + " plot");
text='least squares fitting line, y = '+str(round (popt[0], 9))+' * x + '+str(round (popt[1], 7))
axes.legend(['experimental data', text])

#errorbar
for i in range (len(x_data)):
	x_error[i] = x_error[i] * x_data[i]
	y_error[i] = y_error[i] * y_data[i]

axes.errorbar(x_data, y_data, xerr=x_error, yerr=y_error, color='red',ecolor='black')

#scatter
axes.scatter(x_data, y_data, c='red', linewidths=0)

#show
plt.show()

#save
#plt.savefig('physlabwork_3week_plot.svg')

#plt.figure()

#plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

#plt.xlabel(r'delta_pressure, bar')
#plt.ylabel(r'delta_temp, C^o')

#plt.grid()
#plt.legend(loc='best')

#plt.show()
