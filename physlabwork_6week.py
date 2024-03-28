import pandas as pd
import numpy as np

#read data from ods
name = "physlabwork_6week_37"
all_data = pd.read_excel(name+".ods")
x_data = all_data["t (s)"].dropna().to_numpy()
x_name = "time, s"
x_error = []
#all_data[""].dropna().to_numpy()
y_data = all_data["-ln (V/V_0)"].dropna().to_numpy()
y_name = "-ln(voltage/voltage_0)"
y_error = []
#all_data[""].dropna().to_numpy()

#x_data_2 = all_data['delta P (Pa) (turbo)'].dropna().to_numpy()
#x_name_2 =""
#"x_delta_press_Pa_turbo"
#x_error_2 = all_data['error delta P (turbo)'].dropna().to_numpy()
#y_data_2 = all_data['Q (m3/s) (turbo)'].dropna().to_numpy()
#y_name_2 =""
#"y_flow_m3_div_s_turbo"
#y_error_2 = all_data['error Q (turbo)'].dropna().to_numpy()

#x_data = np.hstack([x_data_1, x_data_2])
#x_name = x_name_1
#x_name_1 +" "+ x_name_2
#x_error = np.hstack([x_error_1, x_error_2])
#y_data = np.hstack([y_data_1, y_data_2])
#y_name = y_name_1
#y_name_1 +" "+ y_name_2
#y_error = np.hstack([y_error_1, y_error_2])

#n=6
#x_data = x_data[:]
#x_error = x_error[:]
#y_data = y_data[:]
#y_error = y_error[:]

import matplotlib.pyplot as plt

#figure
fig, axes = plt.subplots()

#plot
axes.plot(x_data, y_data, 'red')

from scipy.optimize import curve_fit

#errorbar
for i in range (len(x_error)):
        x_error[i] = x_error[i] * x_data[i]
        y_error[i] = y_error[i] * y_data[i]

import random
calc_x_error = []
calc_y_error = []
for i in range(0):
        for j in range(0):
                x=0
                y=0
                if (random.random()>0.5):
                        x = x_data[i] + random.random()*x_error[i]
                else:
                        x = x_data[i] - random.random()*x_error[i]
                if (random.random()>0.5):
                        y = y_data[i] + random.random()*y_error[i]
                else:
                        y = y_data[i] - random.random()*y_error[i]
                calc_x_error.append(float(x))
                calc_y_error.append(float(y))

calc_x_error = np.hstack([x_data, calc_x_error])
calc_y_error = np.hstack([y_data, calc_y_error])
#axes.scatter(calc_x_error, calc_y_error, c='black', linewidths=0.25)

#fit
def func(x, a, b):
	return a*x+b
popt, pcov = curve_fit(func, calc_x_error, calc_y_error)
print (popt)
print (pcov)

#grid
plt.grid()

#fit plots
axes.plot(x_data, func(x_data, popt[0], popt[1]), 'b--')

import math
#additional
axes.set_xlabel(x_name)
axes.set_ylabel(y_name)
t=round((1/popt[0]), 2)
axes.set_title("pressure = 37 torr, ch.time = "+str(t)+" s")
text='least squares fitting line, y = ('+str(round (popt[0], 5))+" +- sqrt("+str(round (pcov[0][0], 4))+')) * x + ('+str(round (popt[1], 5))+" +- sqrt("+str(round (pcov[1][1], 4))+'))'
axes.legend(['experimental data', text])

#axes.errorbar(x_data, y_data, xerr=x_error, yerr=y_error, color='red',ecolor='black')

#scatter
axes.scatter(x_data, y_data, c='red', linewidths=0)

#show
#plt.show()

#save
plt.savefig(name+""+".svg")

#plt.figure()

#plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

#plt.xlabel(r'delta_pressure, bar')
#plt.ylabel(r'delta_temp, C^o')

#plt.grid()
#plt.legend(loc='best')

#plt.show()
