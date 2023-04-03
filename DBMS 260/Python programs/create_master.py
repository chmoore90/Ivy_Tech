ufo_tot = {}
ufo_rate = {}
fed_tot = {}
fed_rate = {}
ter_tot = {}
ter_rate = {}

with open('ufo-totals(norm).csv', 'r') as ut:
    ut.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            ufo_tot[i] = str(ut.readline())[4:-1]

with open('ufo-rates(norm).csv', 'r') as ur:
    ur.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            ufo_rate[i] = str(ur.readline())[4:-1]

with open('fed-totals(norm).csv', 'r') as ft:
    ft.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            fed_tot[i] = str(ft.readline())[4:-1]

with open('fed-rates(norm).csv', 'r') as fr:
    fr.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            fed_rate[i] = str(fr.readline())[4:-1]

with open('ter-totals(norm).csv', 'r') as tt:
    tt.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            ter_tot[i] = str(tt.readline())[4:-1]

with open('ter-rates(norm).csv', 'r') as tr:
    tr.readline()
    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            ter_rate[i] = str(tr.readline())[4:-1]


with open('master_data.csv', 'w') as master:
    master.write('year, ufo_norm_total, ufo_norm_rate, ter_norm_total, ter_norm_rate, fed_norm_total,fed_norm_rate\n')

    for i in range(1970,2017):
        if i == 1993:
            continue
        else:
            master.write(f'{i}{ufo_tot[i]}{ufo_rate[i]}{ter_tot[i]}{ter_rate[i]}{fed_tot[i]}{fed_rate[i]}\n')
