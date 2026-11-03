# Republic City Street Atlas

Public, read-only reference for Avatarverse Property Makers, covering Republic City's Upper and Lower East Side in one continuous map.

- Search the street directory and select a street to highlight every mapped section.
- Pan, zoom, pinch, or jump between Upper and Lower East Side.
- Share direct street links and download the street list as CSV.
- No accounts, external dependencies, build service, or backend required.

The atlas contains 61 finalized street names across 78 retained sections, approved on 3 November 2026.

## GitHub Pages

Serve the `main` branch from **/(root)** in **Settings → Pages → Deploy from a branch**. `.nojekyll` tells GitHub to serve the static files directly. All images and links use relative paths, including on a project Pages URL.

## Maintain the map

`index.html` contains the application, styling, and embedded street register. `data.json` is the canonical street register; `image1.png` is the city/property coverage overview, and `image2.png` and `image3.png` are the original RCEP street plans.

After editing street names or geometry in `data.json`, run:

```sh
python3 build.py
```

Commit both `data.json` and the regenerated `index.html`. The script uses only the Python standard library. CSS and application JavaScript can be edited directly in `index.html`.

To preview locally:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000` in a browser.

## Map alignment

The upper plan is scaled uniformly by 0.9852336516291027 and placed at x=437, y=0. The lower plan begins at x=0, y=901. The combined extent is 1774 × 1716. Street positions and extents come from the finalized RCEP workspace export. Editing statuses and historical review notes are excluded from the public dataset.

## Content

Map imagery and street planning are from the Avatarverse Republic City East Properties project. This repository does not include the private working export or ChatGPT hosting configuration.
