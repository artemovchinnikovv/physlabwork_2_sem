import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rcParams ['figure.figsize'] = [8, 6]

#figure
fig, axes = plt.subplots()

leg=[]
q=1
w=0
show = 0
save = 1
clrr=["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]
for q in range(1,6):
    clr = clrr[q-1]
    #read data from ods
    num = 0
    name = "physlabwork_11week_1"
    #"physlabwork_6week_"+str(num)
    all_data = pd.read_excel(name+".ods")
    x_data = all_data["Q"+str(q)].dropna().to_numpy()
    x_name = "power, uW"
    x_error = all_data["eQ"+str(q)].dropna().to_numpy()
    #all_data[""].dropna().to_numpy()
    y_data = all_data["R"+str(q)].dropna().to_numpy()
    y_name = "resistance, Ohm" 
    y_error = all_data["eR"+str(q)].dropna().to_numpy()
    #all_data[""].dropna().to_numpy()

    c_data = all_data["C"+str(q)].dropna().to_numpy()
    T = c_data[0]

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

    from scipy.optimize import curve_fit

    #errorbar
    import random
    calc_x_error = []
    calc_y_error = []
    for i in range(len(x_data)):
            for j in range(w):
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
    axes.scatter(calc_x_error, calc_y_error, c='black', linewidths=-3.25)

    #fit
    def func(x, a, b):
	    return a*x+b
    popt, pcov = curve_fit(func, calc_x_error, calc_y_error)

    #grid
    plt.grid()

    #fit plots
    axes.plot(x_data, func(x_data, popt[0], popt[1]), clr[0]+'--')

    import math
    error_a = (float(pcov[0][0]))**(1/2)
    error_b = (float(pcov[1][1]))**(1/2)

    error_a = round (error_a, 3)
    error_b = round (error_b, 7)
    #additional
    axes.set_xlabel(x_name)
    axes.set_ylabel(y_name)
    #axes.set_title("T = "+str(T)+" K")
    #text="l.sq.fit.line, y = " + str(round (popt[0], 3))+ " * x " + str(round (popt[1], 7))
    text='fitting line, y = ('+str(round (popt[0], 3))+" +- "+str(error_a)+') * x + ('+str(round (popt[1], 7))+" +- "+str(error_b)+')'
    print(leg)
    leg.append("exp.data, T = "+str(T)+" K")
    leg.append(text)
    axes.errorbar(x_data, y_data, xerr=x_error, yerr=y_error, color=clr, fmt='o', capsize=5)

    #show

    #plt.figure()

    #plt.plot(delta_pressure,delta_temp_at_temp_1, label=r'temp_of_thermostat = 18 C^o')
    #plt.plot(delta_pressure,delta_temp_at_temp_2, label=r'temp_of_thermostat = 30 C^o')
    #plt.plot(delta_pressure,delta_temp_at_temp_3, label=r'temp_of_thermostat = 50 C^o')

    #plt.xlabel(r'delta_pressure, bar')
    #plt.ylabel(r'delta_temp, C^o')

    #plt.grid()
    #plt.legend(loc='best')

    #plt.show()

axes.legend(leg)
#show
if show:
    plt.show()

#save
if save:
    plt.savefig("physlabwork_11week"+"_"+str(q)+"n"+".svg")

