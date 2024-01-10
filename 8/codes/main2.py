import numpy as np
import matplotlib.pyplot as plt

# Constants
B_amplitude = 4e-7
omega = 1.05
phi = -3.14
frequency = 108
t_values = np.linspace(0, 2*np.pi, 1000)  # Adjust the range for time (t) axis

# Function to calculate magnetic field B
def calculate_B(t):
    return B_amplitude * np.sin(omega * t - phi * frequency * t)

# Calculate magnetic field values for the given time range
B_values = calculate_B(t_values)

# Plotting the sine wave curve with adjusted x-axis limits
plt.figure(figsize=(8, 4))
plt.plot(t_values, B_values, label=r'$B = (4 \times 10^{-7})\sin(1.05t - 3.14 \times 10^8t)$', color='blue')
plt.title('Sine Wave Curve of Magnetic Field')
plt.xlabel('Time (t)')
plt.ylabel('Magnetic Field B')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Adjust x-axis limits to show only one wave
plt.xlim(0, 2*np.pi)

plt.legend()
plt.show()
