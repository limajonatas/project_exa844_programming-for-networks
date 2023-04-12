import json
import dataCountry
import dataByGender
import dataByRace


def readData(path):
    with open(path, "r") as file:
        lines = file.readlines()
        file.close()
    return lines


print("Starting the program...")

dateAll = dict()
dateAll["by_gender"] = []
dateAll["by_race"] = []
print("Getting data from the country by gender...", end="")

lines = readData("seedsDataByGender.txt")
for line in lines:
    date = dataByGender.getData(line)
    dateAll["by_gender"].append(date)
    print(".", end="")

print("Getting data from the country by color/Race...", end="")

lines = readData("seedsDataByRace.txt")
for line in lines:
    date = dataByRace.getData(line)
    dateAll["by_race"].append(date)
    print(".", end="")

print("Getting data from the country by Education Level...", end="")

lines = readData("seedsDataEducationLevel.txt")
for line in lines:
    date = dataByRace.getData(line)
    dateAll["by_race"].append(date)
    print(".", end="")

print(".")

file = open("dataAll.json", "w")
string = json.dumps(dateAll, indent=4, ensure_ascii=False).encode("utf-8")
file.write(string.decode())
file.close()
print("Done!")
print("file dataAll.json created!")
