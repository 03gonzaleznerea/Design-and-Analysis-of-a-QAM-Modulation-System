import numpy as np
import matplotlib.pyplot as plt

"""
Computations of the average energy per symbol in terms of d^2 

"""
def compute_average_symbol_energy_corrected(rows, cols):
   
    # Generate the C and B values
    C_values = np.linspace(-(rows - 1) * 1 / 2, (rows - 1) * 1 / 2, rows) #We keep the spacing at one as if it was not affected by it
    B_values = np.linspace(-(cols - 1) * 1 / 2, (cols - 1) * 1 / 2, cols) #We keep the spacing at one as if it was not affected by it
    

     
    # Total number of symbols
    M = 512

    # Compute the energy for each symbol
    total_energy = 0
    for C in C_values:
        for B in B_values:
            total_energy += abs(B + C)**2  # Use the sum of B and C before squaring

    # Compute the average energy
    average_energy = total_energy / M
    
    return average_energy

# Parameters for the QAM constellation
rows = 16  # Number of rows (C values)
cols = 32  # Number of columns (B values)


# Compute the normalized average energy per symbol
average_energy_corrected = compute_average_symbol_energy_corrected(rows, cols)

# Print the result in terms of d^2
print(f"Average energy per symbol (E_s): {average_energy_corrected:.4f} * d^2")


def generate_qam_grid(rows, cols, spacing=1):

    # Generate the C and B values
    C_values = np.linspace(-(rows - 1) * spacing / 2, (rows - 1) * spacing / 2, rows)
    B_values = np.linspace(-(cols - 1) * spacing / 2, (cols - 1) * spacing / 2, cols)

    #Show the computed values C_values and B_values respetively
    print("Computed C_values:",C_values)
    print("Computed B_values:",B_values)

    # Create the grid of points
    C, B = np.meshgrid(C_values, B_values)
    
    return C.flatten(), B.flatten()

# Parameters for the 512-QAM constellation
rows = 16  # Number of rows (C values)
cols = 32  # Number of columns (B values)
spacing = 0.29  # Distance between adjacent points (d)

# Generate the grid
C_flat, B_flat = generate_qam_grid(rows, cols, spacing)

# Plot the 512-QAM constellation grid
plt.figure(figsize=(8, 6))
plt.scatter(B_flat, C_flat, color='green', s=10)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.title("512-QAM Constellation Grid")
plt.xlabel("(B values)")
plt.ylabel("(C values)")
plt.grid(alpha=0.3)
plt.show()  