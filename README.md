# CFB Wainwright fire: Sentinel-5P atmospheric data

Raw, unmodified Sentinel-5P (TROPOMI) exports for Oct. 14–22, 2026, the days around the Oct. 17 fire at CFB Wainwright, Alberta. They are kept so anyone can check the analysis in the [CFB Wainwright fire archive](https://github.com/primerogueinc/cfb-wainwright-fire-archive).

Sentinel-5P measures the atmosphere, not the ground. Its native pixels are about 5.5 × 3.5 km, and Copernicus Browser resamples them on export, so it cannot show the fire itself. It can show the smoke plume: carbon monoxide (CO), aerosol index (AER_AI), nitrogen dioxide (NO2), methane (CH4) and formaldehyde (HCHO). It passes over once a day, in the early afternoon local time.

Each folder `sentinel-5p/<date UTC>/<product>/` holds the files exactly as exported from [Copernicus Browser](https://browser.dataspace.copernicus.eu/), plus a `manifest.json`. The manifest gives the SHA-256 of every file, the frame, the pixel size, the minimum, median and maximum values, and the value over the fire's origin.

## Exports

| Date (UTC) | Product | Files | Window | Note |
|---|---|---|---|---|
| 2026-10-14 | AER_AI | 4 | ~50 × 34 km | Baseline. Partial: aerosol index only, small window. Median index 1.54, 2.16 over the fire site. |

## Adding an export

```
python3 scripts/ingest.py path/to/Browser_images.zip [--note "..."]
```

## Licence

Scripts and documentation: see LICENSE. Data: contains modified Copernicus Sentinel data [2026].

Maintained by Prime Rogue Inc.
