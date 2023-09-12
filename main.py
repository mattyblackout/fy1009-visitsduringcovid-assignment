# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Declare file name
filename = 'Visits_during_covid.csv'

# File Contents:
# Entity, Code, Date, Retail & Recreation, Grocery & Pharmacy, Parks, Transit Stations, Workplaces, Residential

# Read data from file
with open(filename) as data_file:
    lines = data_file.readlines()

for line in lines:
    # Split line data into different categories
    ent, code, date, retailRec, groceryPharm, park, station, work, res = line.strip().split(',')

    # Ignore header line
    if 'Entity' in line:
        pass

    # Read and store data from 1st March (Pre-lockdown) in the appropriate arrays
    if '2020-03-01' in line:
        marchData = [100 + float(retailRec), 100 + float(groceryPharm), 100 + float(park), 100 + float(station),
                     100 + float(work), 100 + float(res)]

    # Read and store data from 1st May (Mid-lockdown) in the appropriate arrays
    if '2020-05-01' in line:
        mayData = [100 + float(retailRec), 100 + float(groceryPharm), 100 + float(park), 100 + float(station),
                   100 + float(work), 100 + float(res)]

    # Read and store data from 1st August (Post-lockdown) in the appropriate arrays
    if '2020-08-01' in line:
        augustData = [100 + float(retailRec), 100 + float(groceryPharm), 100 + float(park), 100 + float(station),
                      100 + float(work), 100 + float(res)]

# Create array of x ticks
x = ["Retail & Recreation", "Grocery & Pharmacy", "Parks", "Transit Stations", "Workplaces", "Residential"]
# Declare line width
width = 0.2

# Configure the spacing between bars
bar1 = np.arange(len(x))
bar2 = bar1 + width
bar3 = bar2 + width

# Plot the data into a bar graph
plt.bar(bar1, marchData, width, label="Pre-Lockdown (1st March 2020)")
plt.bar(bar2, mayData, width, label="Mid-Lockdown (1st May 2020)")
plt.bar(bar3, augustData, width, label="Post-Lockdown (1st August 2020)")

# Formatting
plt.title("The change in visits to various sectors during COVID-19")
plt.xlabel("Sector(s)")
plt.ylabel("Percentage of visits relative to January 2020 (Pre-COVID) (%)")
plt.xticks(bar2, x)
plt.legend()

# Display graph
plt.show()