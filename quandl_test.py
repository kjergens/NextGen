import pandas as pd
import numpy as np
import quandl
import datetime

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# First conda install quandl
# Instructions - https://www.quandl.com/tools/python
# Example code - https://www.palmislandtraders.com/econ136/quandl_data_api.html
# Video - https://www.youtube.com/watch?v=Wedcuxsk0vU

quandl.ApiConfig.api_key = 'xHp4H8JeQxudDrqRysyX'
# nflx = quandl.get("WIKI/NFLX", start_date="2017-06-08", end_date="2017-07-07")
# print(nflx.head())

appl = quandl.get("WIKI/AAPL", rows=50)
print(appl)

appl[['Adj. Close', 'Open']].plot()
plt.show()
