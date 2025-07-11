import matplotlib.pyplot as plt
import numpy as np
import math as m


# constants 
g=9.81  # acceleration due to gravity(m/s**2)

#initial conditions
u= float(input("enter the initial velocity (m/s): "))
theta = float(input("enter the launch angle in degrees: ")) * (np.pi/180) #converting to radians

#time of flight
T = 2 * u * np.sin(theta) / g

#create time intervals
dt = 0.01 #time step
times = np.arange(0,T,dt)

#Calculate x,y cordinates
x=u*np.cos(theta)*times
y=u*np.sin(theta)*times-0.5*g*times**2

#calculating range,maximum height, and time of flight 
#Note: The max height and time of flight can also be derived from kinematic equations without using the plots.
Range = u * np.cos(theta) * T
max_height = (u * np.sin(theta)**2) / (2 * g)

print(f"Range: {Range} m")
print(f"Maximum Height: {max_height} m")
print(f"Time of Flight: {T} s")

#plotting
plt.figure(figsize=(12,6))

#(i) x-y plane (trajectory)
plt.subplot(1,3,1)
plt.plot(x,y)
plt.title('Projectile motion')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.grid(True)

#(ii) x versus t
plt.subplot(1,3,2)
plt.plot(times,x)
plt.title('x vs time')
plt.xlabel('time(s)')
plt.ylabel('x(m)')
plt.grid(True)

#(iii) y versus t 
plt.subplot(1,3,3)
plt.plot(times,y)
plt.title('y vs time')
plt.xlabel('time(s)')
plt.ylabel('y(m)')
plt.grid(True)


plt.show()
