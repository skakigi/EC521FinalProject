import json
import matplotlib.pyplot as plt
from collections import Counter

with open('/Users/jason/Documents/Schoolwork/Fall_2024/EC521/EC521FinalProject/vulnapi_scripts/results.json', 'r') as file:
    data = json.load(file)

# api_count = high_count = med_count = low_count = info_count = 0

# for api in data:
#     api_count += 1
#     high_count += len(data[api]['High'])
#     med_count += len(data[api]['Medium'])
#     low_count += len(data[api]['Low'])
#     info_count += len(data[api]['Info'])

# fig, ax = plt.subplots()
# severities = ['Info', 'Low', 'Medium', 'High']
# counts = [info_count, low_count, med_count, high_count]

# ax.bar(severities, counts)

# ax.set_ylabel('Vulnerabilities Found')
# ax.set_title('Vulnerabilities by Severity')

# plt.show()

info_vulnerabilities = []

for url, vulnerabilities in data.items():
    if "Info" in vulnerabilities:
        info_vulnerabilities.extend(vulnerabilities["Info"])

# Step 3: Count occurrences of each vulnerability using Counter
vulnerability_counts = Counter(info_vulnerabilities)

# Step 4: Create a histogram (bar plot) for the vulnerability counts
# We will sort the counts and create a bar plot
labels, counts = zip(*vulnerability_counts.items())
labels = [label.strip() for label in labels]  # Clean up any leading/trailing spaces

# Step 5: Plot the histogram
plt.figure(figsize=(10, 6))
plt.barh(labels, counts, color='skyblue')
plt.xlabel('Count')
plt.ylabel('Vulnerability')
plt.title('Frequency of "Info" Vulnerabilities')
plt.tight_layout()
plt.show()