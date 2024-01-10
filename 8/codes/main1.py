import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the E value for a given x and t
def calculate_E(x, t):
    return 120 * np.sin(1.05 * x - 3.1e8 * t)

# Generate x values
x_values = np.linspace(0, 10, 1000)

# Set a reasonable time range (adjust as needed)
time_values = np.linspace(0, 1, 1000)

# Create a 2D grid of x and t values
x_grid, t_grid = np.meshgrid(x_values, time_values)

# Calculate E values for each combination of x and t
E_values = calculate_E(x_grid, t_grid)

# Plot the sine wave
plt.figure(figsize=(10, 5))
plt.plot(x_values, E_values[0, :], label='E = 120sin[1.05x - 3.1 x 10^8t] j')

# Set plot labels and title
plt.xlabel('x')
plt.ylabel('E')
plt.title('Sin Wave Curve of Electric field')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
