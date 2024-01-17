import numpy as np
import matplotlib.pyplot as plt

# Function to calculate magnetic field vector B
def magnetic_field(x, t):
    return (4e-7) * np.sin(1.05 * x - 3.14 * 10**8 * t)

# Values for x
x_values = [1, 2, 3]

# Time values with smaller increments for better visualization
time_values = np.linspace(0, 1e-7, 1000)

# Plotting the graphs for each x value
plt.figure(figsize=(10, 6))
for x in x_values:
    B_values = magnetic_field(x, time_values)
    plt.plot(time_values, B_values, label=f'x = {x}')

# Set axis labels and title
plt.xlabel('Time (s)')
plt.ylabel('Magnetic Field (B)')
plt.title('Magnetic Field vs Time')
plt.legend()  # Display legend with x values

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
