# Kelva Process Simulator

A dynamic process engineering simulator for thermal energy storage (TES) systems.
Models networks of unit operations connected by air streams, with time-dependent
mass and energy balances.

---

## Project Structure

    kelva-process-sim/
    ├── sim/                        # core framework
    │   ├── stream.py               # Stream dataclass (mdot, T, P, cp)
    │   ├── base_node.py            # UnitOp abstract base class
    │   ├── graph.py                # graph manager + time loop (coming)
    │   ├── logger.py               # state logging to DataFrame (coming)
    │   ├── visualize_topology.py   # Option 3: static network diagram
    │   ├── visualize_results.py    # Option 1: post-run matplotlib plots
    │   └── visualize_dash.py       # Option 2: live browser dashboard
    ├── nodes/                      # unit operation implementations
    │   ├── boundary.py             # inlet source and outlet sink
    │   ├── heater.py               # resistive heater
    │   ├── heat_exchanger.py       # heat exchanger (coming)
    │   ├── fan.py                  # fan/blower (coming)
    │   └── tes_stack.py            # 1D TES stack physics (coming)
    ├── tests/                      # pytest test suite
    ├── examples/                   # runnable simulation cases
    └── notebooks/                  # Jupyter notebooks for exploration

---

## Setup

    git clone https://github.com/caelittle/kelva-process-sim.git
    cd kelva-process-sim
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

---

## Running a Simulation

Every example supports three run modes:

    # Fast run - no visualization, just prints results to terminal
    python examples/single_tes.py

    # Post-run plots - matplotlib charts saved to PNG after run completes
    python examples/single_tes.py --plot

    # Live dashboard - opens browser at http://localhost:8050, updates as it runs
    python examples/single_tes.py --viz

---

## Visualization Options

### Option 1: Post-run Matplotlib plots (--plot)
- Runs after simulation completes
- One chart per logged variable
- Saved automatically to results.png
- Best for: quick analysis, comparing runs

### Option 2: Live Dash dashboard (--viz)
- Opens at http://localhost:8050 in your browser
- Updates every 500ms as simulation runs
- Shows stream values table + live charts
- Best for: watching TES charge/discharge in real time

### Option 3: Network topology diagram
- Shows nodes and connections as a directed graph
- Saved to topology.png
- Call draw_topology(graph) before running
- Best for: verifying your flowsheet is wired correctly

---

## Key Conventions

- All temperatures in Kelvin
- All pressures in Pascal
- All mass flows in kg/s
- All energy in Joules or Watts
- Every node implements step(dt, inflows) -> outflows and get_state() -> dict
- Stream objects are immutable; nodes return new Stream objects

---

## Status

- [x] Stream dataclass
- [x] UnitOp base class
- [x] ResistiveHeater node
- [x] Boundary nodes (inlet/outlet)
- [x] Visualization framework (all 3 modes)
- [ ] Graph manager + time loop
- [ ] Logger
- [ ] TES stack node (1D physics port)
- [ ] Heat exchanger node
- [ ] Fan/blower node
