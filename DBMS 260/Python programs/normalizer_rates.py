normalized_totals_file = "ter-totals(norm).csv"
rates_file = "ter-rates.csv"
out_filename = "ter-rates(norm).csv"

normalized_totals = {}
rates = {}
normalized_rates = {}

with open(normalized_totals_file, "r") as f:
    f.readline()

    for line in f:
        row = line.strip().split(",")
        year = int(row[0])
        total = float(row[1])
        normalized_totals[year] = total

with open(rates_file, "r") as r:
    r.readline()

    for line in r:
        row = line.strip().split(",")
        year = int(row[0])
        rate = float(row[1])
        rates[year] = rate

sorted_totals = sorted(normalized_totals)
normalized_rates[sorted_totals[0]] = 0

for x in range(len(sorted_totals)):
    if x == len(sorted_totals) - 1:
        break

    curr = sorted_totals[x+1]
    prev = sorted_totals[x]

    normalized_rates[curr] = normalized_totals[curr]*rates[curr]

with open(out_filename, "w") as out:
    out.write('year, normalized rate\n')
    for k, v in normalized_rates.items():
        out.write(f'{k},{v}\n')
