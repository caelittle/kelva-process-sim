"""
Simplest possible flowsheet: inlet -> heater -> outlet
Validates that the node interface and energy balance work.
"""

import sys
sys.path.insert(0, '.')

from nodes.boundary import InletBoundary, OutletBoundary
from nodes.heater import ResistiveHeater

# define nodes
inlet   = InletBoundary("inlet",  mdot=1.0, T=300.0, P=101325.0)
heater  = ResistiveHeater("heater", Q_input=10000.0)   # 10 kW
outlet  = OutletBoundary("outlet")

# manual single timestep — no graph manager yet
dt = 1.0  # seconds

s1 = inlet.step(dt, {})["air_out"]
s2 = heater.step(dt, {"air_in": s1})["air_out"]
outlet.step(dt, {"air_in": s2})

print(f"Inlet  T: {s1.T:.1f} K  ({s1.T - 273.15:.1f} C)")
print(f"Outlet T: {s2.T:.1f} K  ({s2.T - 273.15:.1f} C)")
print(f"dT expected: {heater.Q_input / (s1.mdot * s1.cp):.2f} K")
print(f"dT actual:   {s2.T - s1.T:.2f} K")
print("Energy balance OK" if abs((s2.T - s1.T) - heater.Q_input / (s1.mdot * s1.cp)) < 1e-6 else "ERROR")
