import plotly.plotly as py
import json
from plotly.graph_objs import *

with open('./config.json') as config:
    plotly_user_config = json.load(config)

py.sign_in(plotly_user_config["ascoo"], plotly_user_config["d6k9457d4a"])

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

unique_url = py.plot(data, filename = 'basic-line')
