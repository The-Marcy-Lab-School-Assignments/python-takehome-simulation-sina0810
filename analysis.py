import csv

rows = []
open_count = 0
# 1
with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['resolution_status'] == 'Open':
            open_count += 1
        rows.append(row)
# 2
complaint_count = {}
for row in rows:
    complaint_type = row['complaint_type']
    if complaint_type in complaint_count:
        complaint_count[complaint_type] += 1
    else:
        complaint_count[complaint_type] = 1

maxx = max(complaint_count, key= complaint_count.get)

# 3
borough_count = {}
for row in rows:
    borough = row['borough']
    if borough in borough_count:
        borough_count[borough] += 1
    else:
        borough_count[borough] = 1

sorted_boroughs = sorted(borough_count.keys())


# 4
sorted_complaints = sorted(complaint_count, key=complaint_count.get, reverse=True)

# 5
open_by_borough = {}
for row in rows:
    if row['resolution_status'] == 'Open':
        borough = row['borough']
        if borough in open_by_borough:
            open_by_borough[borough] += 1
        else:
            open_by_borough[borough] = 1
top_borough = max(open_by_borough, key=open_by_borough.get)

# 6
closed_by_borough = {}
for row in rows:
    if row['resolution_status'] == 'Closed':
        borough = row['borough']
        if borough in closed_by_borough:
            closed_by_borough[borough] += 1
        else: 
            closed_by_borough[borough] = 1


# 7
sorted_by_total = sorted(borough_count, key=lambda b: (-borough_count[b], b))
top_3 = sorted_by_total[:3]



with open('output.txt', 'w') as f:
# 1
    f.write(f"Open requests: {open_count}\n\n")
# 2
    f.write(f"Most common complaint type: {maxx} ({complaint_count[maxx]} requests)")
# 3
    f.write("\nRequests per borough:\n")
    for borough in sorted_boroughs:
        f.write(f"- {borough}: {borough_count[borough]}\n")
# 4
    f.write("\nRequests by complaint type:\n")
    for complaint in sorted_complaints:
        f.write(f"- {complaint}: {complaint_count[complaint]}\n")
# 5
    f.write(f"\nBorough with most open requests:  {top_borough} ({open_by_borough[top_borough]} open)")
# 6 
    f.write(f"\nClosure rate by borough:\n")
    for borough in sorted_boroughs:
        rate = round(closed_by_borough[borough] / borough_count[borough] * 100, 1)
        f.write(f"- {borough}: {rate}%\n")
# 7
    f.write(f"\nTop 3 boroughs by total requests:\n")
    for i, borough in enumerate(top_3, 1):
        f.write(f"{i} {borough} ({borough_count[borough]} requests)\n")

print("Output saved to output.txt")





