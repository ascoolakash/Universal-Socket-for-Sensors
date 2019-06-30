import plotly.plotly as py
#import json
from plotly.graph_objs import Scatter, Layout, Figure

import time
import readadc
import datetime

readadc.initialize();
username = 'ascoo'
api_key = 'd6k9457d4a'
stream_token = 'lx3pcmffpp'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
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
while True:
    sensor_data = readadc.readadc(sensor_pin,
                                  readadc.PINS.SPICLK,
                                  readadc.PINS.SPIMOSI,
                                  readadc.PINS.SPIMISO,
                                  readadc.PINS.SPICS)

    millivolts = sensor_data * (3300.0 / 1024.0)
    # 10 mv per degree
    temp_C = ((millivolts - 100.0) / 10.0) - 40.0
    # convert celsius to fahrenheit
    temp_F = (temp_C * 9.0 / 5.0) + 32
    # remove decimal point from millivolts
    millivolts = "%d" % millivolts
    # show only one decimal place for temprature and voltage readings
    temp_C = "%.1f" % temp_C
    temp_F = "%.1f" % temp_F

    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(0.25)
