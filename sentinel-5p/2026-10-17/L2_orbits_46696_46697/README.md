# Sentinel-5P Level 2, Oct. 17, 2026: the two afternoon orbits, pixel by pixel

Added Nov. 27, 2026. Unlike the Copernicus Browser exports elsewhere in this repo (a resampled daily mosaic), these are the native TROPOMI pixels (about 5.5 × 3.5 km) from each orbit, with quality values, clipped to 300 km around the burn centre (52.7645 N, -110.9052 W).

Source: Microsoft Planetary Computer, `sentinel-5p-l2-netcdf`, near-real-time (NRTI) granules. Original file names and SHA-256 in `manifest.json`. Contains modified Copernicus Sentinel data (2026).

| Orbit | Over the burn (MDT) | Products |
|---|---|---|
| 46696 | about 12:55 p.m. | NO2, aerosol index (354/388 nm), aerosol layer height, CO |
| 46697 | about 2:34 p.m. | same |

## What they show

- **Aerosol index, a band moving south-east.** Both orbits show a long SW–NE band of raised UV aerosol index, the same band noted in the Oct. 17 export above. Measured on a line through the burn at right angles to the band (pixels within 40 km of that line, quality ≥ 0.5): the peak sat about **60 km north-west of the burn at 12:55 p.m.** (index 1.4) and about **20–30 km north-west at 2:34 p.m.** (index 1.0–1.1). That is about 35–40 km in 99 minutes, roughly 22–25 km/h toward the south-east. At that rate it would reach the burn at roughly 3:25–3:50 p.m. **Reading:** consistent with a frontal dust or haze line moving through ahead of, or with, the wind shift; the aerosol index alone cannot say whether it is dust, smoke or a cloud-edge effect. An extrapolation, not an observation of the front at the burn.
- **Over the burn itself:** index 0.73 (12:55) and 0.31 (2:34); within 30 km means 0.70 and 0.36, against 0.47 and −0.17 for the ring 150–300 km out. Slightly raised, inside the band's influence; no separate plume from the burn can be picked out at this pixel size.
- **NO2:** no plume. At 2:34 p.m. the burn pixel is 0.88 × 10^15 molec/cm² (quality 0.90); within 30 km mean 1.5, max 3.3, against 1.2 for the outer ring. At 12:55 the area is mostly cloud-masked.
- **CO and aerosol layer height:** no usable pixels over the burn on either orbit (cloud). The few layer-height values that pass the quality filter within 30 km at 2:34 p.m. sit at about 11 km and are likely cloud-contaminated; not used.

`s5p_oct17_maps.png`: aerosol index and NO2 for both orbits. Grey is no data or low quality.
