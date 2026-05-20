from dataclasses import dataclass


@dataclass
class Stream:
    mdot: float
    T: float
    P: float
    cp: float = 1006.0

    @property
    def enthalpy_flow(self) -> float:
        return self.mdot * self.cp * self.T

    @property
    def is_valid(self) -> bool:
        return self.mdot >= 0 and self.T > 0 and self.P > 0

    def __repr__(self):
        return (f"Stream(mdot={self.mdot:.4f} kg/s, "
                f"T={self.T:.1f} K, P={self.P:.0f} Pa)")
