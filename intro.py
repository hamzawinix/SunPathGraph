from pvlib import solarposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


tz = 'Asia/Amman'
lat, lon = 31.9, 35.9
times = pd.date_range('2021-01-01 00:00:00', '2022-01-01', closed='left',
                      freq='H', tz=tz)

solarpos = solarposition.get_solarposition(times, lat, lon)
# remove nighttime
solarpos = solarpos.loc[solarpos['apparent_elevation'] > 0, :]

fig, ax = plt.subplots()
# points = ax.scatter(solarpos.azimuth, solarpos.apparent_elevation, s=2,
#                     c=solarpos.index.dayofyear, label=None)
# fig.colorbar(points)

points = ax.scatter(solarpos.azimuth, solarpos.apparent_elevation, s=10,
                    c=solarpos.index.dayofyear,cmap='Wistia')

#nice, plasma ,accent, pink , Wistia



for hour in np.unique(solarpos.index.hour):
    # choose label position by the largest elevation for each hour
    subset = solarpos.loc[solarpos.index.hour == hour, :]
    height = subset.apparent_elevation
    pos = solarpos.loc[height.idxmax(), :]
    ax.text(pos['azimuth'], pos['apparent_elevation'], str(hour))

for date in pd.to_datetime(['2021-01-21','2021-02-21', '2021-03-21','2021-04-21','2021-05-21', '2021-06-21','2021-07-21','2021-08-21', '2021-09-21','2021-10-21','2021-11-21', '2021-12-21']):
    times = pd.date_range(date, date+pd.Timedelta('24h'), freq='5min', tz=tz)
    solarpos = solarposition.get_solarposition(times, lat, lon)
    solarpos = solarpos.loc[solarpos['apparent_elevation'] > 0, :]
    label = date.strftime('%Y-%m-%d')
    ax.plot(solarpos.azimuth, solarpos.apparent_elevation, label=label)

ax.figure.legend(loc='upper left')
ax.set_xlabel('Solar Azimuth (degrees)')
ax.set_ylabel('Solar Elevation (degrees)')

plt.show()