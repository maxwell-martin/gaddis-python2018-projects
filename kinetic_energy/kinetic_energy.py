def kinetic_energy(mass_kg, velocity_mps):
    return 0.5 * mass_kg * velocity_mps **2

mass = float(input("Enter the mass (kg): "))
velocity = float(input("Enter the velocity (m/s): "))

ke = kinetic_energy(mass, velocity)

print("Kinetic energy is:", format(ke, ".2f"))
