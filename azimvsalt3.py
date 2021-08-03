from pvlib import solarposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tz = 'Asia/Amman'
lat, lon = 31.9539, 35.9106
times = pd.date_range('2021-01-01 00:00:00', '2022-01-01', closed='left',
                      freq='H', tz=tz)

solpositions = solarposition.get_solarposition(times, lat, lon)
# remove nighttime
solpositions = solpositions.loc[solpositions['apparent_elevation'] > 0, :]

fig, ax = plt.subplots()

#fig2,ax2 = plt.subplots()

# points = ax.scatter(solpositions.azimuth, solpositions.apparent_elevation, s=2,
#                     c=solpositions.index.dayofyear, label=None)
#fig.colorbar(points)

# for hour in np.unique(solpositions.index.hour):
#     # choose label position by the largest elevation for each hour
#     subset = solpositions.loc[solpositions.index.hour == hour, :]
#     height = subset.apparent_elevation
#     pos = solpositions.loc[height.idxmax(), :]
#     ax.text(pos['azimuth'], pos['apparent_elevation'], str(hour))

for date in pd.to_datetime(['2021-03-21', '2021-06-21', '2021-12-21']):
    times = pd.date_range(date, date+pd.Timedelta('24h'), freq='5min', tz=tz)
    solpositions = solarposition.get_solarposition(times, lat, lon)
    solpositions = solpositions.loc[solpositions['apparent_elevation'] > 0, :]
    label = date.strftime('%Y-%m-%d')
    #plot azimuth vs elevation
    ax.plot(solpositions.azimuth, solpositions.apparent_elevation, label=label)
    

ax.figure.legend(loc='upper left')
ax.figure.legend(loc='upper center')
ax.set_xlabel('Solar Azimuth (degrees)')
ax.set_ylabel('Solar Elevation (degrees)')

plt.show()


