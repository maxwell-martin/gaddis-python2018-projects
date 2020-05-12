moons_mean_radius = { "Io":1821.6, "Europa":1560.8,
                      "Ganymede":2634.1, "Callisto":2410.3 }
moons_surface_gravity = { "Io":1.796, "Europa":1.314,
                          "Ganymede":1.428, "Callisto":1.235 }
moons_orbital_period = { "Io":1.769, "Europa":3.551,
                          "Ganymede":7.154, "Callisto":16.689 }

moon = input("Enter name of a Galilean moon of Jupiter: ").rstrip(" ").lstrip(" ")

if moon not in moons_mean_radius:
    print(moon, "is not a Galilean moon of Jupiter.")
else:
    print("Mean radius:", moons_mean_radius[moon])
    print("Surface gravity:", moons_surface_gravity[moon])
    print("Orbital Period:", moons_orbital_period[moon])
