import threading
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


class LiveDashboard:

    def __init__(self, port=8050):
        self.port = port
        self.data = []
        self.app = Dash(__name__)
        self._setup_layout()
        self._setup_callbacks()

    def _setup_layout(self):
        self.app.layout = html.Div([
            html.H2("Kelva Process Simulator - Live Dashboard",
                    style={"fontFamily": "Arial", "color": "#2c3e50",
                           "padding": "20px"}),
            dcc.Interval(id="interval", interval=500, n_intervals=0),
            html.Div(id="stream-table",
                     style={"padding": "0 20px", "fontFamily": "Arial"}),
            html.Div(id="charts",
                     style={"padding": "0 20px"})
        ])

    def _setup_callbacks(self):
        @self.app.callback(
            [Output("stream-table", "children"),
             Output("charts", "children")],
            [Input("interval", "n_intervals")]
        )
        def update(n):
            if not self.data:
                return html.P("Waiting for simulation data..."), html.Div()

            df = pd.DataFrame(self.data)
            latest = df.iloc[-1]

            rows = [html.Tr([html.Th("Variable"), html.Th("Value")])]
            for col in df.columns:
                if col != "time":
                    rows.append(html.Tr([
                        html.Td(col),
                        html.Td(f"{latest[col]:.3f}")
                    ]))
            table = html.Table(rows, style={
                "borderCollapse": "collapse",
                "width": "400px",
                "marginBottom": "20px"
            })

            numeric_cols = [c for c in df.columns if c != "time"]
            charts = []
            for col in numeric_cols:
                charts.append(dcc.Graph(
                    figure={
                        "data": [{"x": df["time"].tolist(),
                                  "y": df[col].tolist(),
                                  "type": "line",
                                  "name": col}],
                        "layout": {"title": col,
                                   "height": 250,
                                   "margin": {"t": 40, "b": 40},
                                   "xaxis": {"title": "Time (s)"},
                                   "plot_bgcolor": "#f9f9f9"}
                    },
                    style={"width": "48%", "display": "inline-block",
                           "margin": "1%"}
                ))

            return table, html.Div(charts)

    def update(self, t: float, state: dict):
        row = {"time": t}
        row.update(state)
        self.data.append(row)

    def start(self):
        thread = threading.Thread(
            target=lambda: self.app.run(port=self.port, debug=False),
            daemon=True
        )
        thread.start()
        print(f"Dashboard running at http://localhost:{self.port}")
        print("Open that URL in your browser.")
