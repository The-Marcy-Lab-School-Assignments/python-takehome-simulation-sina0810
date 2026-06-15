import csv

rows = []
open_count = 0

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['resolution_status'] == 'Open':
            open_count += 1
        rows.append(row)

complaint_count = {}
for row in rows:
    complaint_type = row['complaint_type']
    if complaint_type in complaint_count:
        complaint_count[complaint_type] += 1
    else:
        complaint_count[complaint_type] = 1

maxx = max(complaint_count, key= complaint_count.get)
print(maxx)

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_count}\n\n")
    f.write(f"Most common complaint type: {maxx} ({complaint_count[maxx]} requests)")

print("Output saved to output.txt")