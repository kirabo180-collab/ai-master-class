# This week focuses on JavaScript.
# Use this terminal to practise Python logic
# that mirrors what you are doing in the browser.

# Replicate JS array methods in Python
fruits = ['mango', 'banana', 'apple']
fruits.append('grape')   # push
print(fruits)
print(fruits.pop())      # pop
print(len(fruits))       # length
import urllib.request, json
# Replicate what the Fetch API does in Python
# Make a GET request and handle the response
url = 'https://httpbin.org/get'
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())
print('Status: 200 OK')
print('Origin IP:', data.get('origin', 'unknown'))
import json
# Practise converting between Python objects and JSON strings
# This mirrors what JS does with JSON.stringify and JSON.parse
obj = {"tool": "AI Summariser", "version": 1, "active": True}
js_string = json.dumps(obj)
print("Serialised:", js_string)
parsed = json.loads(js_string)
print("Tool name:", parsed['tool'])
import urllib.request, json
# Build a simple data fetcher that returns formatted output
# Like a mini backend endpoint would
def fetch_data(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"error": str(e)}

result = fetch_data('https://httpbin.org/json')
print(json.dumps(result, indent=2))
# Jua Kali job quotation calculator
def buildQuote(jobType, materialCost, labourDays, dailyRate):
    labourCost = labourDays * dailyRate;
    subtotal = materialCost + labourCost;
    vat = subtotal * 0.16;
    total = subtotal + vat;
    return {
       "job": jobType,
       "materials": materialCost,
       "labour": labourCost,
       "vat": round(vat),
       "total": round(total)
  }

jobs = [
  buildQuote("Steel door installation", 12000, 2, 2500),
  buildQuote("Floor tiling (45 sqm)", 8100, 3, 2000),
  buildQuote("Carpentry: 6 chairs", 4800, 4, 1800),
]

for q in jobs:
  print(f"Job: {q['job']}")
  print(f"Materials: KES {q['materials']}")
  print(f"Labour: KES {q['labour']}")
  print(f"VAT (16%): KES {q['vat']}")
  print(f"TOTAL: KES {q['total']}")
  print("--------------------")
