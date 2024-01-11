import numpy as np
import matplotlib.pyplot as plt

# Function to calculate electric field vector E
def electric_field(x, t):
    return 120 * np.sin(1.05 * x - 3.1 * 10**8 * t)

# Values for x
x_values = [1, 2, 3]

# Time values with smaller increments for better visualization
time_values = np.linspace(0, 1e-7, 1000)

# Plotting the graphs for each x value
plt.figure(figsize=(10, 6))
for x in x_values:
    E_values = electric_field(x, time_values)
    plt.plot(time_values, E_values, label=f'x = {x}')

# Set axis labels and title
plt.xlabel('Time (s)')
plt.ylabel('Electric Field (E)')
plt.title('Electric Field vs Time')
plt.legend()  # Display legend with x values

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
