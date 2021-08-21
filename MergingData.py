import csv
"""
data = []
with open ('dataset_2.csv', 'r') as f:
    csvreader = csv.reader(f)
    for ro in csvreader:
        data.append(ro)
headers = data[0]
planets = data[1:]
for i in planets:
    i[2] = i[2].lower()
planets.sort(key=lambda planets:planets[2])
with open ('dataset_sorted.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets)
"""
dataset1 = []
dataset2 = []
with open ('dataset_1.csv', 'r') as f:
    csvreader = csv.reader(f)
    for ro in csvreader:
        dataset1.append(ro)

with open ('dataset_sorted.csv', 'r') as f:
    csvreader = csv.reader(f)
    for ro in csvreader:
        dataset2.append(ro)

headers1 = dataset1[0]
planets1 = dataset1[1:]
headers2 = dataset2[0]
planets2 = dataset2[1:]
headerFinal = headers1+headers2
planetsFinal = []
for index, i in enumerate(planets1):
    planetsFinal.append(planets1[index]+planets2[index])
with open('finalPlanets.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headerFinal)
    csvwriter.writerows(planetsFinal)