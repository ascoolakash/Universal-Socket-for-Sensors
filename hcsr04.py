import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import usonic
import datetime

usonic.initialize()
print usonic.reading(0)

username = 'ascoo'
api_key = 'd6k9457d4a'
stream_token = 'lx3pcmffpp'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=2000
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

# temperature sensor connected channel 0 of mc
#i = 0
stream = py.Stream(stream_token)
stream.open()
print usonic.reading(0)
#the main sensor reading loop
while True:
	print usonic.reading(0)
        sensor_data = usonic.reading(0)
        stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
        #i += 1
        # delay between stream posts
        time.sleep(3)
