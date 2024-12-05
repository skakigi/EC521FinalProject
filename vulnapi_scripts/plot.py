import json
import matplotlib.pyplot as plt
from collections import Counter
import os

# Step 1: Load the JSON data
output_dir = "/Users/jason/Documents/Schoolwork/Fall_2024/EC521/EC521FinalProject/vulnapi_scripts/plots"
os.makedirs(output_dir, exist_ok=True)

with open('/Users/jason/Documents/Schoolwork/Fall_2024/EC521/EC521FinalProject/vulnapi_scripts/results.json', 'r') as file:
    data = json.load(file)

# Step 2: Initialize lists to collect vulnerabilities by type
vulnerabilities_by_type = {}
# Step 3: Iterate through each URL and its vulnerabilities
for url, vulnerabilities_data in data.items():
    vuln_type = vulnerabilities_data.get('Type', 'Unknown')  # Get the type of the vulnerability
    
    # If this type isn't already in the dictionary, add it with an empty list
    if vuln_type not in vulnerabilities_by_type:
        vulnerabilities_by_type[vuln_type] = []
    
    # Add this vulnerability to the corresponding type
    vulnerabilities_by_type[vuln_type].extend(vulnerabilities_data["Info"])
    vulnerabilities_by_type[vuln_type].extend(vulnerabilities_data["Medium"])

for type in vulnerabilities_by_type.keys():
    vulnerability_counts = Counter(vulnerabilities_by_type[type])
    labels, counts = zip(*vulnerability_counts.items())
    labels = [label.strip() for label in labels]  # Clean up any leading/trailing spaces

    # Step 5: Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.barh(labels, counts, color='skyblue')
    plt.xlabel('Count')
    plt.ylabel('Vulnerability')
    plt.title(f'Vulnerabilities of Type: {type}')
    plt.tight_layout()

    plot_filename = os.path.join(output_dir, f"{type}_vulnerabilities.png")
    plt.savefig(plot_filename)

    # Close the plot to avoid memory issues (especially when saving multiple plots)
    plt.close()

print(f"Plots saved to {output_dir}")
