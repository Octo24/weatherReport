import csv

f_obj = open("en_climate_hourly_AB_3020035_10-2023_P1H.csv")
reader = csv.reader(f_obj)
for line in reader:
    print(line)

# look into config parser