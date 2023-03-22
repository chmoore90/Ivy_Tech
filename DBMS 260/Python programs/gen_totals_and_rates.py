in_file = "fed_emerg - cleaned.csv"
out_file_tot = "fed-totals.csv"
out_file_rat = "fed-rates.csv"
y_column = 2

totals = {}
rates = {}

#reading
with open(in_file, "r", encoding="utf-8") as f:
    f.readline()

    for line in f:
        row = line.strip().split(",")
        year = row[y_column-1][-4:]

        if year in totals:
            totals[year] += 1
        else:
            totals[year] = 1

    sorted_totals = sorted(totals)

#write totals
with open(out_file_tot, "w") as out_tot:
    out_tot.write('year, total\n')
    for t in sorted_totals:
        out_tot.write(f"{t},{totals[t]}\n")

#write rates
rates[sorted_totals[0]] = 0

for x in range(len(sorted_totals)):
    if x == len(sorted_totals) - 1:
        break

    prev = totals[sorted_totals[x]]
    curr = totals[sorted_totals[x+1]]

    rates[sorted_totals[x+1]] = (curr-prev)/(prev)

with open(out_file_rat, "w") as out_rat:
    out_rat.write('year, rates\n')
    for k, v in rates.items():
        out_rat.write(f'{k},{v}\n')
