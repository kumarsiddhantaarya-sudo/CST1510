"""
RECORD CHECK  -  my version
===========================

Name  : Siddhant Aarya Kumar
Lane  : IT
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt
#pandas handles the data and tables, matplotlib draws the chart.
folder = r"C:\Users\Fortress\Documents\CST1510\Week06_Pandas\Week 06 - Pandas\LAB"
df = pd.read_csv(folder + r"\records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100
#Added a percent column by dividng the value by the limit then multiplying by 100. The pandas do this for all the rows at once so no loop is required.
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
#Also added a status column using .apply() that checks if the percent is OVERLIMIT, WARNING or OK using lambda which is a small function that takes one percent value and returns a label.
print(df.groupby("status").size())
#Group the rows by status
df.to_csv(folder + r"\records_complete.csv", index=False)
#This saves the new full table with the percent and status columns into a new csv file called records_complete.csv
#The index=False stops pandas from writing the 0,1,2,3... row numbers into the file.
df["status"].value_counts().plot(kind="bar", title="Records by status")
#This counts how many records have each status, then draw those counts as a bar chart.
plt.tight_layout()
#This adjusts the spaces in the table so the labels and the title arent cut off in the bar chart.
plt.savefig(folder + r"\status_counts.png")
plt.show()
#Displays the chart in a window.