"""
HOSTNAME CHECK  -  my version
===========================

Name  :  Siddhant
Lane  :  IT      
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
with open("HOSTNAME.txt", "w") as f:
    f.write("SRV-01,81,100\n")
    f.write("SRV-02,150,100\n")
    f.write("SRV-03,35,100\n")
    f.write("SRV-04,104,100\n")
#with open("HOSTNAME.txt", "w") as f: creates a new text file with the hostname information, the gb used and the total gb.
#\n creates a new line
def load_records(path):
    """Read hostname, used, total lines from a file and return a list of dicts."""
    hostnames = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            hostname, used, total = line.split(",")
            hostnames.append({
                "Hostname": hostname,
                "Used": float(used),
                "Total": float(total),})
    return hostnames
#load_records reads each line, splits it into hostname, used and total, converts the numbers to float, and returns all the hostnames as a list of dicts.
#split(",") turns "SRV-01,81,100" into ["SRV-01", "81", "100"]
try:
    hostnames = load_records("HOSTNAME.txt")
except FileNotFoundError:
    print("HOSTNAME.txt not found")
    hostnames = []
#hostnames now holds the loaded data. If the file is missing, a message would print and hostnames would be an empty list, with no error
#try and except lets us see the error and handle the error. For example if there is an error, another code will take place instead of an error taking place and stopping the code
over_count = 0
with open("the_results.txt", "w") as out:
    for host in hostnames:
        if host["Used"] > host["Total"]:
            status = "OVER LIMIT"
            over_count += 1
        else:
            status = "OK"
#if the used is over the total it will print OVER LIMIT, when it is less than it will print OK
        print(f"{host['Hostname']}: {status}")
        out.write(f"{host['Hostname']},{status}\n")
#Every hostname was printed and also written to the_results.txt as hostname, status, and over_count went up by 1 each time a hostname was OVER LIMIT.
print(f"Hostnames over limit: {over_count}")