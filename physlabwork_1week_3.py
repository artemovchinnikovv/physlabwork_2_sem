import numpy as np

import matplotlib.pyplot as plt

#create massives
a=1/(18+273)
b=1/(30+273)
c=1/(50+273)
x_T = [a, b, c]
y_u = [0.96984925, 0.8626506, 0.75]

#figure
fig, axes = plt.subplots()

#plot
axes.plot(x_T, y_u, 'red')
axes.scatter(x_T, y_u, c='red', linewidths=0)

from scipy.optimize import curve_fit

#fit
def func(x, a, b):
	return a*x+b
popt_1, pcov_1 = curve_fit(func, x_T, y_u)
print (popt_1)
print (pcov_1)

#additional
axes.set_xlabel('1/temp_of_thermostat, 1/K')
axes.set_ylabel('u_JT, K/bar')
axes.set_title('u_JT versus temp_of_thermostat plot');
text_1='y = '+str(round (popt_1[0], 2))+' * x + '+str(round (popt_1[1], 2))
axes.legend(['u_JT(T)', text_1])

y_uu=[func(x_T[0], popt_1[0], popt_1[1]), func(x_T[1], popt_1[0], popt_1[1]), func(x_T[2], popt_1[0], popt_1[1])] #bug
#axes.plot(x_T, func(x_T, popt_1[0], popt_1[1]), 'r--') doesnt work and I dont know why

#fit plots
axes.plot(x_T, y_uu, 'r--')
#axes.plot(x_T, func(x_T, popt_1[0], popt_1[1]), 'r--')
#must be this

error = [(0.00704067)**(1/2), (0.00587567)**(1/2), (0.00397769)**(1/2)]
#errorbar
axes.errorbar(x_T, y_u, xerr=0, yerr=error, color='red',ecolor='black')

#grid
plt.grid()

#show
#plt.show()

#save
plt.savefig('physlabwork_1week_plot_dt_dp_3.svg')

#plt.figure()

#plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
#plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

#plt.xlabel(r'delta_pressure, bar')
#plt.ylabel(r'delta_temp, C^o')

#plt.grid()
#plt.legend(loc='best')

#plt.show()
