import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Convert to JSON string
json_text = json.dumps(daily_log)
print("Type:", type(json_text))
print("JSON:", json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nPretty JSON:")
print(pretty)
import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print("Type:", type(data))
print("Steps:", data["steps"])
print("Cold shower:", data["cold_shower"])
print("Protocol:", data["protocol"])
# Writing JSON to a file (use in VS Code):
with open("log.json", "w") as f:
    json.dump(daily_log, f, indent=2)

# Reading JSON from a file (use in VS Code):
with open("log.json", "r") as f:
    data = json.load(f)
import json

# Simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)
import json

# Simulated API response with nested data
api_json = '''
{
  "client": "James Omondi",
  "week": 1,
  "daily_logs": [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"}
  ]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f"  {log['day']}: {log['steps']} steps ({status})")
import json

# A welding workshop stores job records as JSON
job_json = '''
{
  "workshop": "Kamau Metalworks",
  "location": "Gikomba, Nairobi",
  "jobs": [
    {"client": "Wanjiru",  "item": "gate",        "material": "mild steel", "quote_kes": 28000, "paid": true},
    {"client": "Otieno",   "item": "window grills","material": "angle iron", "quote_kes": 14500, "paid": false},
    {"client": "Mwangi",   "item": "door frame",   "material": "hollow tube","quote_kes": 9800,  "paid": true}
  ]
}
'''

data = json.loads(job_json)
print("Workshop:", data["workshop"])
print("Location:", data["location"])
print()

total = 0
paid = 0
for job in data["jobs"]:
    status = "PAID" if job["paid"] else "PENDING"
    print(f"  {job['client']}: {job['item']} - KES {job['quote_kes']:,} [{status}]")
    total += job["quote_kes"]
    if job["paid"]:
        paid += job["quote_kes"]

print(f"\nTotal quoted: KES {total:,}")
print(f"Collected:    KES {paid:,}")
print(f"Outstanding:  KES {total - paid:,}")   
import json

responses = [
    '{"steps": 9200, "protocol": "OMAD"}',
    'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")