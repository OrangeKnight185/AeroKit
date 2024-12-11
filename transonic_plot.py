from matplotlib import pyplot as plt
import numpy as np

GAMMA = 1.4
CP0 = -0.41

PG_theory = lambda M, CP0: CP0 / np.sqrt(1 - M*M)
isentropic_pressure = lambda M: (2 / (GAMMA*M*M)) * (((1 + 0.5*(GAMMA-1)) / (1 + 0.5*(GAMMA-1)*M*M))**(GAMMA/(1-GAMMA)) - 1)

mach_range = np.arange(0.6, .95, 0.001)
PG_data = PG_theory(mach_range, CP0)
isentropic_data = isentropic_pressure(mach_range)

plt.plot(mach_range, PG_data)
plt.plot(mach_range, isentropic_data)
plt.title("NACA 0012 Graphical Approach using Python")
plt.xlabel("Mach Number")
plt.ylabel("Pressure Coefficient")
plt.legend(["PG Theory", "Isentropic Presure"])
plt.grid()
plt.savefig("NACA0012.png", dpi=300)
