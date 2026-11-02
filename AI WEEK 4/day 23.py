import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())
import io
# Simulate file content
file_data = """"Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

# Simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()
print("Full file content:")
print(content)
import io

file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

f = io.StringIO(file_data)
lines = f.readlines()

print(f"Number of lines: {len(lines)}")
print()
for line in lines:
    line = line.strip()  # Remove newline character at end
    print("Line:", line)
import io
# Start with existing content
file_data = "Steps : 9200\nWater: 8 glasses\nProtocol: OMAD\n"
# Simulate append
file_data += "Pages read: 30\n"
file_data += "workout: bench press 5*5 at 80kgs\n"
print("File after appending:")
print(file_data)
import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print("Parsed log:")
for key, value in log.items():
    print(f"  {key}: {value}")