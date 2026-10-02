"""
RECORD CHECK  -  my version
===========================

Name  :  Siddhant Aarya Kumar
Lane  :  IT      (delete two)
Date  :  27/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = ""      # : replace with an input() call
first = 0.0     # : replace with an input() call, converted
second = 0.0    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = 0.0   # 
percent = 0.0      # 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you

Hostname = input("Enter Hostname:  ")
GB_used = float(input("Enter the GB used:  "))
Total_GB = float(input("Enter the total GB:  "))

Free_GB = Total_GB - GB_used
Percentage = (GB_used / Total_GB) * 100

print("=" * 35)
print(f"Hostname check - {Hostname}")
print("=" * 35)
print(f" {'GB used':<10}: {GB_used:10.2f}")
print(f" {'Total GB':<10}: {Total_GB:10.2f}")
print(f" {'Free GB':<10}: {Free_GB:10.2f}")
print(f" {'Percentage':<10}: {Percentage:10.2f} %")
print("=" * 35)
# I used {'GB used':<10} to allign the labels to the left in a 10 character wide field so everything lines up.
# {GB_used:10.2f} was used to to allign all the numbers to the right in a 10 character wide field so all the numbers line up.
# I was making a few mistakes when formatting, I kept forgetting how to format all the values. I'm still not very confident with f string, I need to do more examples and practice.
# Also made simple mistakes and errors which included not using " " and also forgot to use float. I fixed those problems.
# When placing all values as 0, it gives me a ZeroDivisionError.