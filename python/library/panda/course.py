import pandas as pd

course = pd.read_csv("course.csv")

print(course.to_string())

print(course.columns)
