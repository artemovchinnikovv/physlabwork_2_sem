import matplotlib.pyplot as plt

#create massives
x_T = [1/(18+273),1/(30+273), 1/(50+273)]
y_u = [0.96984925, 0.8626506, 0.75]

#figure
fig, axes = plt.subplots()

#plot
axes.plot(x_T, y_u, 'red')
#axes.scatter(delta_pressure, delta_temp_at_temp_1, c='red', linewidths=0)

from scipy.optimize import curve_fit

#additional
axes.set_xlabel('temp_of_thermostat, K')
axes.set_ylabel('u_JT, K/Pa')
axes.set_title('u_JT versus temp_of_thermostat plot');

#errorbar
#axes.errorbar(delta_pressure, delta_temp_at_temp_1, xerr=0.05, yerr=0.019, color='red',ecolor='black')
#axes.errorbar(delta_pressure, delta_temp_at_temp_2, xerr=0.05, yerr=0.019, color='green',ecolor='black')
#axes.errorbar(delta_pressure, delta_temp_at_temp_3, xerr=0.05, yerr=0.019, color='blue',ecolor='black')

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
