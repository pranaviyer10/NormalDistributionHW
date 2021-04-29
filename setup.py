import csv 
import numpy as np

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks in Percentage"]))
            days_present.append(float(row["Dats Present"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corroef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path = "Student_Marks_vs_Days_Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()