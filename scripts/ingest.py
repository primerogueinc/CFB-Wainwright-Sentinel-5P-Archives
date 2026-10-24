"""Ingest a raw Copernicus Browser Sentinel-5P export (zip) into sentinel-5p/<date UTC>/<product>/.
Usage: python3 scripts/ingest.py EXPORT.zip [--note "..."]
Copies files unchanged; writes manifest.json (SHA-256 per file, frame, pixel size, stats, value over the fire)."""
import sys, os, re, json, hashlib, zipfile, tempfile, glob, shutil
import numpy as np
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIRE = (-110.9214, 52.7764)
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def main(zin, note):
    import rasterio
    tmp = tempfile.mkdtemp(); zipfile.ZipFile(zin).extractall(tmp)
    files = sorted(f for f in glob.glob(tmp + "/**/*", recursive=True) if os.path.isfile(f))
    groups = {}
    for f in files:
        m = re.match(r"(\d{4}-\d{2}-\d{2})-\d{2}_\d{2}_\d{4}-\d{2}-\d{2}-\d{2}_\d{2}_Sentinel-5P_([A-Z0-9]+(?:_AI)?)_(.+)\.(tiff?|jpe?g|png)$", os.path.basename(f), re.I)
        if not m: print("skip", os.path.basename(f)); continue
        groups.setdefault((m.group(1), m.group(2).upper()), []).append(f)
    for (date, prod), fs in sorted(groups.items()):
        dest = os.path.join(REPO, "sentinel-5p", date, prod); os.makedirs(dest, exist_ok=True)
        layers = {}
        for f in fs:
            name = os.path.basename(f); info = {"bytes": os.path.getsize(f), "sha256": sha(f)}
            if name.lower().endswith((".tif", ".tiff")):
                r = rasterio.open(f); a = r.read(1).astype("float64"); v = a[np.isfinite(a)]
                info.update({"bands": r.count, "shape": list(r.shape), "bounds": [round(x, 4) for x in r.bounds],
                             "pixel_km_approx": [float(round(r.res[0] * 111.32 * np.cos(np.radians(52.77)), 2)), round(r.res[1] * 110.95, 2)],
                             "raw": "(Raw)" in name})
                if "(Raw)" in name:
                    i, j = r.index(*FIRE)
                    info["valid_frac"] = round(float(v.size) / a.size, 3)
                    info["stats"] = None if not v.size else {"min": float(f"{v.min():.4g}"), "median": float(f"{np.median(v):.4g}"), "max": float(f"{v.max():.4g}"),
                                     "at_fire": round(float(a[i, j]), 6) if np.isfinite(a[i, j]) and 0 <= i < a.shape[0] and 0 <= j < a.shape[1] else None}
            layers[name] = info
        man = {"source": "Copernicus Browser export (Sentinel Hub), received from Prime Rogue", "date_utc": date, "product": prod, "note": note or "",
               "original_upload": os.path.basename(zin), "original_upload_sha256": sha(zin), "files": layers,
               "licence": "Contains modified Copernicus Sentinel data [2026]"}
        mp = os.path.join(dest, "manifest.json")
        if os.path.exists(mp):  # second export for the same day/product: merge
            old = json.load(open(mp)); old["files"].update(layers); man["files"] = old["files"]
            ups = old.get("original_uploads") or [{"name": old.get("original_upload"), "sha256": old.get("original_upload_sha256")}]
            ups = [u for u in ups if u["name"] != man["original_upload"]] + [{"name": man["original_upload"], "sha256": man["original_upload_sha256"]}]
            man.pop("original_upload"); man.pop("original_upload_sha256"); man["original_uploads"] = ups
            if old.get("note") and not man["note"]: man["note"] = old["note"]
        for f in fs: shutil.copy2(f, dest)
        json.dump(man, open(os.path.join(dest, "manifest.json"), "w"), indent=1)
        r0 = next((v for v in layers.values() if v.get("stats")), {})
        print(date, prod, len(fs), r0.get("shape"), r0.get("pixel_km_approx"), r0.get("stats"))
    shutil.rmtree(tmp)
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else None)
