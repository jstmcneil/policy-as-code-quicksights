import sys
import yaml
import json

# Get our results file open. Extract non compliant items.
with open(sys.argv[1], "r") as stream:
    data = yaml.safe_load(stream)
    non_compliant_items = data.get('not_compliant').items()

# Loop through non-compliant items and extract data to our lists.
resource = {}
policy = {}
for index, items in enumerate(non_compliant_items):
    # Add infringed resource to list.
    if not items[0] in resource:
        resource[items[0]] = 1
    else:
        resource[items[0]] += 1
        
    # Add policy infringement to list.
    if not items[1][0]["rule"] in policy:
        policy[items[1][0]["rule"]] = 1
    else:
        policy[items[1][0]["rule"]] += 1

# Add data to json dictionary; subsequently dump that json to a file to store as an artifact.
metrics_json = {"@timestamp": "", "file_name": "", "resource": "", "policy": ""}
metrics_json["resource"] = resource
metrics_json["policy"] = policy
metrics_json["file_name"] = sys.argv[1]
metrics_json["@timestamp"] = sys.argv[2]
with open("metrics.json", "w+") as f:
    json.dump(metrics_json, f)