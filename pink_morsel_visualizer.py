import pandas
from dash import Dash, html, dcc

from plotly.express import line

DATA_PATH = "./formatted_data.csv"

COLORS = {
    "prim": "#44CCCC",
    "sec": "#888888",
    "font": "#EEEEEE"
}

data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

# Create visualization
def generate_vis(data):
    chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
    chart.update_layout(
        plot_bgcolor=COLORS["prim"],
        paper_bgcolor=COLORS["sec"],
        font_color=COLORS["font"]
    )
    return chart

visualization = dcc.Graph(
    id="visualization",
    figure=generate_vis(data)
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["sec"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# Region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "100%"
    }
)


# Region picker callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    figure = generate_vis(trimmed_data)
    return figure

# Layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_picker
    ]
)

if __name__ == '__main__':
    dash_app.run_server()