import sys
sys.path.insert(0, '.')

import matplotlib.pyplot as plt
from nodes.boundary import InletBoundary, OutletBoundary
from nodes.heater import ResistiveHeater

# create nodes
inlet  = InletBoundary("inlet", mdot=1.0, T=300.0, P=101325.0)
heater = ResistiveHeater("heater", Q_input=10000.0)
outlet = OutletBoundary("outlet")

# time settings
dt    = 1.0     # seconds per timestep
t_end = 3600.0  # 1 hour

# storage for results
times      = []
T_inlet    = []
T_outlet   = []
Q_total    = []

# time loop
t = 0.0
Q_accumulated = 0.0

while t < t_end:
    s1 = inlet.step(dt, {})["air_out"]
    s2 = heater.step(dt, {"air_in": s1})["air_out"]
    outlet.step(dt, {"air_in": s2})

    Q_accumulated += heater.Q_input * dt  # joules added this step

    times.append(t)
    T_inlet.append(s1.T - 273.15)
    T_outlet.append(s2.T - 273.15)
    Q_total.append(Q_accumulated / 1e6)   # convert to MJ

    t += dt

print(f"Run complete: {len(times)} timesteps")
print(f"Inlet  T: {T_inlet[-1]:.1f} C  (constant)")
print(f"Outlet T: {T_outlet[-1]:.1f} C  (constant)")
print(f"Total energy added: {Q_total[-1]:.2f} MJ")

# plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

ax1.plot(times, T_inlet,  label="Inlet T",  linestyle="--", color="blue")
ax1.plot(times, T_outlet, label="Outlet T", linestyle="-",  color="red")
ax1.set_ylabel("Temperature (C)")
ax1.set_xlabel("Time (s)")
ax1.set_title("Heater: Inlet vs Outlet Temperature over 1 Hour")
ax1.legend()
ax1.grid(True)

ax2.plot(times, Q_total, color="orange")
ax2.set_ylabel("Cumulative Energy Added (MJ)")
ax2.set_xlabel("Time (s)")
ax2.set_title("Total Energy Input over Time")
ax2.grid(True)

plt.tight_layout()
plt.savefig("examples/heater_over_time.png")
plt.show()
print("Plot saved to examples/heater_over_time.png")
