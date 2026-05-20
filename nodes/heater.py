"""
Resistive heater node.
Adds fixed electrical power Q_input (W) to the air stream.
"""

from sim.base_node import UnitOp
from sim.stream import Stream


class ResistiveHeater(UnitOp):

    def __init__(self, name: str, Q_input: float):
        super().__init__(name)
        self.Q_input = Q_input      # heater power (W)
        self.T_outlet = None        # tracked for logging

    def step(self, dt: float, inflows: dict[str, Stream]) -> dict[str, Stream]:
        inlet = inflows["air_in"]

        # energy balance: Q = mdot * cp * (T_out - T_in)
        dT = self.Q_input / (inlet.mdot * inlet.cp)
        T_out = inlet.T + dT
        self.T_outlet = T_out

        outlet = Stream(
            mdot=inlet.mdot,
            T=T_out,
            P=inlet.P,
            cp=inlet.cp
        )
        return {"air_out": outlet}

    def get_state(self) -> dict:
        return {
            "Q_input_W": self.Q_input,
            "T_outlet_K": self.T_outlet
        }
