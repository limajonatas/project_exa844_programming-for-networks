import json

from generateData import dataByGender, dataByRace, dataByEducationLevel


def readData(path):
    with open(path, "r") as file:
        lines = file.readlines()
        file.close()
    return lines


print("Starting the program...")

dateAll = dict()
dateAll["by_gender"] = []
dateAll["by_race"] = []
dateAll["by_education_level"] = []
print("Getting data from the country by gender...", end="")

linesDataByGender = readData("seeds/seedsDataByGender.txt")
linesDataByRace = readData("seeds/seedsDataByRace.txt")
linesDataEducationLevel = readData("seeds/seedsDataEducationLevel.txt")

for line in linesDataByGender:
    date = dataByGender.getData(line)
    dateAll["by_gender"].append(date)
    print(".", end="")

print("\nGetting data from the country by color/Race...", end="")

for line in linesDataByRace:
    date = dataByRace.getData(line)
    dateAll["by_race"].append(date)
    print(".", end="")

print("\nGetting data from the country by Education Level...", end="")

for line in linesDataEducationLevel:
    date = dataByEducationLevel.getData(line)
    dateAll["by_education_level"].append(date)
    print(".", end="")

print()

file = open("dataAll.json", "w")
string = json.dumps(dateAll, indent=4, ensure_ascii=False).encode("utf-8")
file.write(string.decode())
file.close()
print("Done!")
print("file dataAll.json created with success!")
