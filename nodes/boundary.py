from sim.base_node import UnitOp
from sim.stream import Stream


class InletBoundary(UnitOp):

    def __init__(self, name: str, mdot: float, T: float, P: float):
        super().__init__(name)
        self.stream = Stream(mdot=mdot, T=T, P=P)

    def step(self, dt: float, inflows: dict[str, Stream]) -> dict[str, Stream]:
        return {"air_out": self.stream}

    def get_state(self) -> dict:
        return {"T_K": self.stream.T, "mdot_kg_s": self.stream.mdot}


class OutletBoundary(UnitOp):

    def __init__(self, name: str):
        super().__init__(name)
        self.last_inflow = None

    def step(self, dt: float, inflows: dict[str, Stream]) -> dict[str, Stream]:
        self.last_inflow = inflows["air_in"]
        return {}

    def get_state(self) -> dict:
        if self.last_inflow is None:
            return {}
        return {
            "T_K": self.last_inflow.T,
            "mdot_kg_s": self.last_inflow.mdot
        }
