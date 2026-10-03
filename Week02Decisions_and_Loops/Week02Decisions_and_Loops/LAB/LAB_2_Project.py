"""
RECORD CHECK  -  my version
===========================

Name  :  Siddhant
Lane  :  IT      
Date  :  03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

Hostname = input("Enter Hostname: ")
Used_GB = float(input("Enter GB used: "))
Total_GB = float(input("Enter the total GB: "))
#Over here the user enters the hostname as a text, the Used GB and the Total GB are converted into a decimal using float
Difference = Total_GB - Used_GB
Percentage = (Used_GB / Total_GB) * 100
#In order to calculate the difference I did the Total GB - The Used GB which was entered by the user
#The percentage of how much GB is used was calculated by dividing the Used GB by the Total GB then multiplying it by 100
if Percentage >= 100:
    status = "OVER LIMIT"
elif Percentage >= 90:
    status = "WARNING"
else:
    status = "OK"
#The if condition is used to see if the Used GB percentage has passed or is equal to the Total
#Elif only checks if the first condition was false
#Else is whatever is below the Elif condition, it is the fase of the Elif condition
print("=" * 35)
print(f" Hostname CHECK - {Hostname}")
print("=" * 35)
print(f" {'Used':<10}: {Used_GB:10.2f}")
print(f" {'Total':<10}: {Total_GB:10.2f}")
print(f" {'Difference':<10}: {Difference:10.2f}")
print(f" {'Percent':<10}: {Percentage:10.2f} %")
print(f" {'Status':<10}: {status:>10}")
print("=" * 35)
#The use of 10.2f is to show 2 decimal places, which was one of the conditions I needed to add for this task.