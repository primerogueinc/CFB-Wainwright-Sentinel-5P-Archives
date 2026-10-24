# CFB Wainwright fire: Sentinel-5P atmospheric data

Raw, unmodified Sentinel-5P (TROPOMI) exports for Oct. 14–22, 2026, the days around the Oct. 17 fire at CFB Wainwright, Alberta. They are kept so anyone can check the analysis in the [CFB Wainwright fire archive](https://github.com/primerogueinc/cfb-wainwright-fire-archive).

Sentinel-5P measures the atmosphere, not the ground. Its native pixels are about 5.5 × 3.5 km, and Copernicus Browser resamples them on export, so it cannot show the fire itself. It can show the smoke plume: carbon monoxide (CO), aerosol index (AER_AI), nitrogen dioxide (NO2), methane (CH4) and formaldehyde (HCHO). It passes over once a day, in the early afternoon local time.

Each folder `sentinel-5p/<date UTC>/<product>/` holds the files exactly as exported from [Copernicus Browser](https://browser.dataspace.copernicus.eu/), plus a `manifest.json`. The manifest gives the SHA-256 of every file, the frame, the pixel size, the minimum, median and maximum values, and the value over the fire's origin.

## Exports

| Date (UTC) | Product | Files | Window | Note |
|---|---|---|---|---|
| 2026-10-14 | AER_AI | 4 | ~50 × 34 km | Baseline. Full coverage. Median index 1.54 (340/380 nm), 2.16 over the fire site. |
| 2026-10-14 | CO | 2 | ~50 × 34 km | 53% of pixels valid; fire site masked. Median 0.0255 mol/m². |
| 2026-10-14 | NO2 | 2 | ~50 × 34 km | 25% valid; fire site masked. Exported twice (identical). |
| 2026-10-14 | HCHO | 2 | ~50 × 34 km | 17% valid; values at noise level. |
| 2026-10-14 | CH4 | 2 | ~50 × 34 km | No valid pixels (quality-filtered, likely cloud). |
| 2026-10-14 | SO2 | 4 | ~50 × 34 km | No valid pixels. TIFF and JPG exports. |
| 2026-10-14 | O3 | 1 | ~50 × 34 km | Visualised layer only (no raw values). |
| 2026-10-17 | CO | 1 | ~790 × 550 km (Banff to east of Saskatoon) | Visualised layer only. Fire site is no-data: a cloud band runs SW–NE through it. Clear patches near Edmonton, Calgary, Saskatoon. |

Most gas products are quality-filtered under cloud, so on cloudy days only the aerosol index covers the area. From Oct 16 on, exports cover a wider window and only AER_AI, CO and NO2.
## Pass times

`pass_times.csv` (from `scripts/pass_times.py`) lists each daytime pass. On Oct. 17 the pass that saw the base was at **2:34 p.m. MDT** (20:34 UTC), 240 km off-track: during the fire, before the GOES-18 peak at 3:30 p.m. Exports are daily mosaics, so a day's file can combine two passes.

## Adding an export

```
python3 scripts/ingest.py path/to/Browser_images.zip [--note "..."]
```

## Licence

Scripts and documentation: see LICENSE. Data: contains modified Copernicus Sentinel data [2026].

Maintained by Prime Rogue Inc.
