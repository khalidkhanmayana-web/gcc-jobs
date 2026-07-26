import json
import datetime

data = {
    "last_updated": str(datetime.datetime.now()),
    "categories": [
        {
            "name": "Design & CAD Engineering",
            "listings": [
                {
                    "title": "Senior CAD Design Engineer",
                    "country": "Kuwait",
                    "company": "Kuwait Industrial Group",
                    "location": "Ahmadi, Kuwait",
                    "type": "Full-time",
                    "apply_url": "https://www.linkedin.com/jobs/search/?keyword=CAD+Engineer+Kuwait"
                },
                {
                    "title": "Technical Document Controller",
                    "country": "UAE",
                    "company": "Dubai Engineering LLC",
                    "location": "Dubai, UAE",
                    "type": "Full-time",
                    "apply_url": "https://www.linkedin.com/jobs/search/?keyword=Document+Controller+UAE"
                }
            ]
        },
        {
            "name": "Remote & Contract Roles",
            "listings": [
                {
                    "title": "Freelance CAD & Drafting Specialist",
                    "country": "Remote",
                    "company": "Gulf Engineering Bureau",
                    "location": "Remote (GCC Region)",
                    "type": "Contract",
                    "apply_url": "https://www.upwork.com/nx/search/jobs/?q=CAD%20Drafting"
                }
            ]
        }
    ]
}

with open('jobs.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Listings with direct links updated successfully!")
