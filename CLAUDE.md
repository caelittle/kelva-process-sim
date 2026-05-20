# Kelva Process Simulator

## What this is
A dynamic process engineering simulator for thermal energy storage (TES) systems.
Models networks of unit operations (TES stacks, heat exchangers, heaters, fans)
connected by air streams, with time-dependent mass and energy balances.

## Architecture
- `sim/` — core framework: Stream, UnitOp base class, graph manager, time loop
- `nodes/` — unit operation implementations
- `tests/` — pytest; run with `pytest tests/`
- `examples/` — runnable end-to-end cases

## Key conventions
- All temperatures in Kelvin
- All pressures in Pascal
- All mass flows in kg/s
- All energy in Joules or Watts
- Every node implements `step(dt, inflows) -> outflows` and `get_state() -> dict`
- Stream objects are immutable; nodes return new Stream objects

## Current status
Scaffold only. Physics not yet implemented.
TES 1D model physics are validated separately (HTML/JS file, to be ported).
