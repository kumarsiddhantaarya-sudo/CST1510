"""
HOSTNAME CHECK  -  my version
===========================

Name  :  Siddhant Aarya Kumar
Lane  :  IT     
Date  :  10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def divider():
    print("=" * 34)
#This prints a line of 34 "=". I made it a function so I dont need to print("="*34) in all the sections I need to.
def check(value, limit):
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent
#This returns both the free GB and the percentage of the free GB.
def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

Hostname = input("Server name: ")
used_gb = float(input("Used: "))
total_gb = float(input("Total: "))
free, percentage = check(used_gb, total_gb)
status = status_of(percentage)
#The input lets the user type the value they want instead of the value being being fixed. I used float to convert the text into a decimal.
divider()
print(f"  HOSTNAME CHECK  -  {Hostname}")
divider()

print(f"  {'Used GB':<12}: {used_gb:>11.2f}")
print(f"  {'Total GB':<12}: {total_gb:>11.2f}")
print(f"  {'Free GB':<12}: {free:>11.2f}")
print(f"  {'Percent':<12}: {percentage:>10.2f} %")
print(f"  {'Status':<12}: {status:>11}")
divider()
#<12 lines up all the colons
#11.2f right alligns the number in 11 spaces with 2 decimal places.