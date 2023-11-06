list_of_temps = []

with open("GITHUB/weatherReport/en_climate_hourly_AB_3020035_10-2023_P1H.csv") as data:
    next(data)  # Skip the header row
    for line in data:
        columns = line.strip().split(",")

        # Check if there are at least 10 columns
        if len(columns) >= 10:
            temperature = columns[9].strip('""')  # Remove leading and trailing double quotes

            # Check if the temperature is not empty
            if temperature:
                list_of_temps.append(float(temperature))

if list_of_temps:
    max_temperature = max(list_of_temps)
    print(f"Maximum temperature: {max_temperature}°C")

with open("GITHUB/weatherReport/outputs.txt", "w") as output_counts:
    output_counts.write("OUTPUT FILE:\n")
    output_counts.write(f"Maximum temperature: {max_temperature} degrees celsius")