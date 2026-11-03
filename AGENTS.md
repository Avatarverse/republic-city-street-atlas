# Atlas maintenance

- This is a public read-only static site. Preserve that behavior.
- `data.json` is canonical. Run `python3 build.py` after data changes and commit the updated `index.html` as well.
- Preserve finalized names and retained sections unless the user explicitly asks for a correction. Repeated names can represent different sections of the same street.
- Keep paths relative so GitHub Pages project URLs work.
- Never add editor statuses, old review notes, credentials, or private source exports to the public files.
- No dependency installation or framework is needed. Check affected interactions in a browser for UI changes.
