import os
import pandas as pd
from openpyxl import load_workbook

theXLSXName = input("Lütfen dosya ismini giriniz: " + "\n")

print(os.getcwd())
file = pd.read_excel(theXLSXName)

theDict = {}

workbook = load_workbook(filename=theXLSXName)
sheet = workbook.active

df = pd.read_excel(theXLSXName)
fileLen = len(df)

for i in range(2, fileLen + 2):
    currentPerson = (sheet[f"A{i}"].value).split(",")

    if currentPerson[0] not in theDict:
        theDict[f"{currentPerson[0]}"] = int(currentPerson[-1])
    else:
        if currentPerson[0] in theDict:
            theDict[f"{currentPerson[0]}"] += int(currentPerson[-1])


f = open("theresult.txt", "w", encoding="utf-8")

users = theDict.keys()

for i, j in theDict.items():
    if j >= 45:
        print(i)
        f.write(i + "\n")

f.close()
