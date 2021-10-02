# import packages 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'font.size': 25, 'legend.fontsize': 20, 'axes.titlesize': 24})


# list of constants 
AU = 1.496*10**11
G = 39.5 # Gravitational constant in astronomical units
M_centr = float(input("Enter the Central Body's Mass in Solar Mass, then press 'Enter'"))  # Planet's mass

# Set up the initial conditions
mu = G * M_centr
Sat = []

x_sat = float(input("Satellite's x position in AU"))
y_sat = float(input("Satellite's y position in AU"))
vx_sat = float(input("Satellite's x velocity in AU/yr"))
vy_sat = float(input("Satellite's y velocity in AU/yr"))

N = float(input('Enter the amount of total steps'))
T = float(input("Enter the simulation's total duration in years"))

Duration = T * N
t = np.linspace(0., T, N)
dt = t[1] - t[0]

# Different gravitational circumstances
def a_g (orb_rad):
    return (G * M_centr/ orb_rad**3)

# Relativity-adjusted gravitational formula here:


# Euler-Cromer method
def EC_Simulation (Planet, grav_func, time):
    # Read the initial conditions
    x = [Planet[0]]
    y = [Planet[1]]
    v_x = [Planet[2]]
    v_y = [Planet[3]]
    
    # FOR loop for the Euler-Cromer Integration
    for i in range(len(time)-1):
        r = np.sqrt(x[i]**2 + y[i]**2)
        
        # For x, y, v_x, and v_y formulas, see the lab report section Q1 
        v_x.append(v_x[i] - grav_func(r) * x[i] * dt)
        v_y.append(v_y[i] - grav_func(r) * y[i] * dt)    

        x.append((x[i] + v_x[i] * dt - grav_func(r) * x[i] * dt**2))
        y.append((y[i] + v_y[i] * dt - grav_func(r) * y[i] * dt**2))

    return np.array([x, y, v_x, v_y]) # Returns the planet'sorbital parameters in a packed array

Output = EC_Simulation(Sat, a_g, t)

Output_x = Output[0]
Output_y = Output[1]
Output_vx = Output[2]
Output_vy = Output[3]

fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))

# Generates the phase plot
ax1.plot(Output_x, Output_y)
ax1.scatter(0, 0, label="Central Body", color='Orange') # Adds the Sun's location for reference
ax1.set_title("Satellite's Orbit Over" + str(T) + "Earth Year")
ax1.set_xlabel("x (AU)")
ax1.set_ylabel("y (AU)")
ax1.legend()