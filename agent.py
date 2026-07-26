import json
import datetime

# Sample data representing fetched jobs
data = {
    "last_updated": str(datetime.datetime.now()),
    "listings": [
        {
            "title": "Senior CAD Design Engineer",
            "country": "Kuwait",
            "company": "Kuwait Industrial Group",
            "location": "Ahmadi, Kuwait"
        },
        {
            "title": "Document Controller",
            "country": "UAE",
            "company": "Dubai Engineering LLC",
            "location": "Dubai, UAE"
        }
    ]
}

# Write to jobs.json
with open('jobs.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Job listings updated successfully!")
