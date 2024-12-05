import json
import matplotlib.pyplot as plt

with open('results.json', 'r') as file:
    data = json.load(file)

api_count = high_count = med_count = low_count = info_count = 0

for api in data:
    api_count += 1
    high_count += len(data[api]['High'])
    med_count += len(data[api]['Medium'])
    low_count += len(data[api]['Low'])
    info_count += len(data[api]['Info'])

fig, ax = plt.subplots()
severities = ['Info', 'Low', 'Medium', 'High']
counts = [info_count, low_count, med_count, high_count]

ax.bar(severities, counts)

ax.set_ylabel('Vulnerabilities Found')
ax.set_title('Vulnerabilities by Severity')

plt.show()