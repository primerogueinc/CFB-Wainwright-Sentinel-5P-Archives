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
| 2026-10-16 | AER_AI | 4 | ~790 × 550 km | Baseline, day before. Full coverage. Base 0.40, ~10 km NE 0.66 (Oct. 17: 0.38 and 0.52). Regional streaks present, scene median 0.53. Comparison: `sentinel-5p/aer_ai_oct16_vs_oct17.png`. |
| 2026-10-17 | AER_AI | 4 | ~790 × 550 km | Full coverage. Long SW–NE bands of raised index across the whole region (frontal cloud/regional haze). Base 0.38 (scene median 0.03); 0.5–0.9 within ~10 km to the NE. No distinct plume from the base separable from the regional band. |
| 2026-10-18 | AER_AI | 4 | ~790 × 550 km | After. Full coverage. Base 0.24, ~10 km NE 0.25, scene median 0.27. Three-day comparison: `sentinel-5p/aer_ai_oct16_17_18.png`. |
| 2026-10-18 | CO | 4 | ~790 × 550 km | TIFF + earlier JPG. 71% valid. At the base 0.0295 mol/m², the scene median (0.0297); no residual plume. |

Most gas products are quality-filtered under cloud, so on cloudy days only the aerosol index covers the area. From Oct 16 on, exports cover a wider window and only AER_AI, CO and NO2.
## Finding so far

The Oct. 17 pass (2:34 p.m. MDT) shows no smoke signal from the fire that can be separated from regional weather: the aerosol index at and just downwind of the base was the same as, or lower than, the day before (base 0.40 / 0.38 / 0.24 on Oct. 16 / 17 / 18; ~10 km NE 0.66 / 0.52 / 0.25). CO over the base was masked by cloud on Oct. 17 and at background level on Oct. 18. Sentinel-5P neither confirms nor rules out anything about the fire; it does not show a large elevated plume before 2:34 p.m.

## Pass times

`pass_times.csv` (from `scripts/pass_times.py`) lists each daytime pass. On Oct. 17 the pass that saw the base was at **2:34 p.m. MDT** (20:34 UTC), 240 km off-track: during the fire, before the GOES-18 peak at 3:30 p.m. Exports are daily mosaics, so a day's file can combine two passes.

## Adding an export

```
python3 scripts/ingest.py path/to/Browser_images.zip [--note "..."]
```

## Licence

Scripts and documentation: see LICENSE. Data: contains modified Copernicus Sentinel data [2026].

Maintained by Prime Rogue Inc.
