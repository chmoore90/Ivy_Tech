from gen_totals_and_rates import totals
out_filename = "ter-totals(norm).csv"

normalized = {}
sorted = sorted(totals)
x = max(totals.values())

for k, v in totals.items():
    n = v/x
    normalized[k] = n

with open(out_filename, "w") as out:
    out.write(f'year, normalized total\n')
    for k, v in normalized.items():
        out.write(f'{k},{v}\n')
