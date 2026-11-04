# Example: solo founder

Alex runs a tiny product company. Org starts with Jarvis as master agent, a two-seat council, and three teams: Product, Money, Health.

Open the map:

```bash
# from repo root after scripts/update_org.py
python3 -m http.server 8765
# http://127.0.0.1:8765/interface/?org=examples/solo-founder/org.json
```

Or open `interface/index.html` (embedded demo data may show the last embedded org; regenerate with the update script pointed at this `org.json`).
