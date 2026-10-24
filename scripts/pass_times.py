"""Predict Sentinel-5P daytime passes over CFB Wainwright (52.77N, 110.90W) from a two-line element set (TLE).
TLE: Space-Track via keeptrack.space, epoch 2026-10-23 16:44 UTC. Time of closest approach of the ground track, 10 s steps.
TROPOMI's swath is about 2,600 km wide, so passes with cross-track distance under about 1,300 km see the base (edge pixels are larger)."""
from skyfield.api import EarthSatellite, load, wgs84
import numpy as np, datetime as dt
ts = load.timescale()
sat = EarthSatellite("1 42969U 17064A   26296.69747661  .00000033  00000+0  36597-4 0  9998", "2 42969  98.8052 237.9712 0000690  84.5758 275.5497 14.19497062467792", "S5P", ts)
t = ts.utc(2026, 10, 13, 0, np.arange(0, 10 * 24 * 360) / 6.0)
sp = wgs84.subpoint_of(sat.at(t)); lat, lon = sp.latitude.radians, sp.longitude.radians
la0, lo0 = np.radians(52.77), np.radians(-110.90)
d = 6371 * np.arccos(np.clip(np.sin(lat) * np.sin(la0) + np.cos(lat) * np.cos(la0) * np.cos(lon - lo0), -1, 1))
print("pass_utc,pass_mdt,cross_track_km,sees_base")
for i in range(1, len(d) - 1):
    if d[i] < d[i - 1] and d[i] <= d[i + 1] and d[i] < 1500 and lat[i + 1] > lat[i]:
        u = t[i].utc_datetime(); print(f"{u:%Y-%m-%d %H:%M},{u - dt.timedelta(hours=6):%Y-%m-%d %H:%M},{d[i]:.0f},{'yes' if d[i] < 1250 else 'edge'}")
