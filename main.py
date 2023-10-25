with open("weatherReport/en_climate_hourly_AB_3020035_10-2023_P1H.csv") as data:
   csv = data.read()
# print(csv)
list_of_temps = []
# f_obj = open("weatherReport/en_climate_hourly_AB_3020035_10-2023_P1H.csv")
# data = f_obj.read()
for line in csv:
    columns = line.split(",")
    # column 10
    if len(columns) >= 10:
        list_of_temps.append(columns[9])
        print(list_of_temps)

list_of_numbers = []
for temp in list_of_temps:
    numbers = float(temp.replace('""', ""))
    list_of_numbers.append(numbers)
print(max(list_of_numbers))
# for line in csv:
#     if "," in line:
#         fields = line.split(",")

# print(fields)

# data = open("en_climate_hourly_AB_3020035_10-2023_P1H.csv")
# csv = data.read()
# print(csv)