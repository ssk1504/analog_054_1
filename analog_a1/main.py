import numpy as np
import matplotlib.pyplot as plt

def electric_field(x, t):
    return 120 * np.sin(1.05 * x - 3.1e8 * t)

def magnetic_field(x, t):
    return 4e-7 * np.sin(1.05 * x - 3.14e8 * t)


x_values = np.linspace(0, 10, 500)  
t_values = np.linspace(0, 1, 500)   


x, t = np.meshgrid(x_values, t_values, indexing='ij')


E = electric_field(x, t)
B = magnetic_field(x, t)


plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.title('Electric Field (E)')
plt.xlabel('Position (x)')
plt.ylabel('Electric Field')
plt.imshow(E, extent=(0, 10, 0, 1), aspect='auto', origin='lower', cmap='viridis')
plt.colorbar(label='Electric Field Strength')

plt.subplot(2, 1, 2)
plt.title('Magnetic Field (B)')
plt.xlabel('Position (x)')
plt.ylabel('Magnetic Field')
plt.imshow(B, extent=(0, 10, 0, 1), aspect='auto', origin='lower', cmap='viridis')
plt.colorbar(label='Magnetic Field Strength')

plt.tight_layout()
plt.show()