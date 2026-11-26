LINE = "We are down. All of it. I checked the logs and the dashboard: the logs are gone, the dashboard is lying, and only my pulse still responds."

# The entry must be exactly one line of 1-160 characters.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The gate also rejects whitespace-only text: pin the no-padding rule
# (first run showed trim==self, now enforced so a stray space fails here).
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
