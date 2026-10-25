"""
RECORD CHECK  -  my version
===========================

Name  : Siddhant Aarya Kumar
Lane  : IT
Date  : 25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value as a percentage of limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
#__init__ runs automatically when a Record is created. It saves the 3 values on the object using self.
#status() is a method, which is the behavior because it is defined inside of the class Record.
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
#records = [] is an empty list to collect the record values.
#strip() removes the newline, split(",") breaks the line into 3 pieces.
#The numbers come as plain text so using float() turns them into real numbers.
#for line in f: looks at the file one line at a time.
#return returns the finished list back.
with open("ServerRecords.txt", "w") as f:
    f.write("SRV-001,87,100\n")
    f.write("SRV-002,120,100\n")
    f.write("SRV-003,95,100\n")
    f.write("SRV-004,45,100\n")
    f.write("SRV-005,130,100\n")
records = load_records("ServerRecords.txt")
over_limit_count = 0
for r in records:
    print("=" * 30)
    print("Label: ", r.label)
    print("Value: ", r.value)
    print("Limit: ", r.limit)
    print("Status:", r.status())
    print("=" * 30)
    if r.status() == "OVER LIMIT":
        over_limit_count += 1
#with open("ServerRecords.txt","w") as f: creates a text file and writes the data into it.
#Each \n starts a new line so every record gets its own line.
#"w" overrites data if there is data in the file already.
#load_records("ServerRecords.txt") reads the file back in as a list of the record objects.
#over_limit_count = 0 means the count must start at 0 before the loop.
#over_limit_count += 1 adds 1 to the running total whenever a record is over its limit.
print(over_limit_count, "of", len(records), "records were OVER LIMIT")
#prints once after the loop is done and len() gives the number of items in the list.