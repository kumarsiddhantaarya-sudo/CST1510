"""
RECORD CHECK  -  my version
===========================

Name  :  Siddhant Aarya Kumar
Lane  :  IT  
Date  :  16/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


FILENAME = "status_lines.txt"
#Messy raw lines, inconsistent spacing and capitalization, one blank line, and one bad line (used=unknown) to test that the script doesn't crash.
raw_lines = """  Srv-01 , used=87 , total=100
SRV-02,used=120,total=100
srv-03 ,  USED = 95 , Total= 100

  LAB-04,used=60,total=80
Srv-05 , used=100 , total=100
srv-06,used=unknown,total=100
  SRV-07 ,used=91.5, total=100
"""
#This saves the raw lines to a file ("w" = write mode, replaces the file if it exists).
with open(FILENAME, "w") as f:
    f.write(raw_lines)

def parse_line(raw_line):
    """Turn one messy status line into a clean dict."""
#Remove outer whitespace, then lowercase the whole line so that "SRV-02", "USED" and "Total" all become lowercase in one step.
    line = raw_line.strip().lower()
#Split at the FIRST comma only, hostname on the left, the rest on the right.
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip()       #This removes spaces around the hostname

    fields = {}                            #will hold used and total
    for piece in rest.split(","):          #one piece per key=value pair
        key, value = piece.split("=")      #split "used = 95" into "used " and " 95"
#Strip the spaces off both parts, convert the value to a number, and store it under the clean key.
        fields[key.strip()] = float(value.strip())

#Returns a clean dict. If a field is missing, fields["used"] raises KeyError.
    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}
def percent_of(record):
    """Return usage as a percentage of the total."""
    return record["used"] / record["total"] * 100

def status_of(record):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK."""
    percent = percent_of(record)
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

results = []      #(record, status) for every line that parsed successfully
bad_lines = []    #raw text of every line that could not be parsed
with open(FILENAME) as f:
    for line in f:            #reads the file one line at a time
        if not line.strip():  #a blank line is empty after stripping skip it (parse_line would crash on it)
            continue

        try:
            record = parse_line(line)         #all the cleaning logic lives in parse_line
        except (ValueError, KeyError):
#ValueError: bad number or extra "=" and the keyerror: missing used/total.
            bad_lines.append(line.strip())
            continue
        results.append((record, status_of(record)))
#Print the table. In each f-string, "<10" left-aligns in a 10-character column and ">8" right-aligns in an 8-character column, so every row lines up.
WIDTH = 47
print("=" * WIDTH)
print("IT STATUS REPORT".center(WIDTH))        #center the title across the table width
print("=" * WIDTH)
print(f"{'HOSTNAME':<10}{'USED':>8}{'TOTAL':>8}{'USAGE':>9}  {'STATUS':<10}")
print("-" * WIDTH)

for record, status in results:
    percent = percent_of(record)
#".1f" shows one decimal place, and the "%" is plain text after the number.
    print(f"{record['hostname']:<10}{record['used']:>8.1f}{record['total']:>8.1f}"
          f"{percent:>8.1f}%  {status:<10}")
print("-" * WIDTH)

flagged = [s for _, s in results if s != "OK"]
print(f"Summary: {len(results)} records, {len(flagged)} flagged")

#List any lines that could not be parsed, only if there were some.
if bad_lines:
    print(f"\nCould not parse ({len(bad_lines)}):")
    for bad in bad_lines:
        print(f"  {bad}")