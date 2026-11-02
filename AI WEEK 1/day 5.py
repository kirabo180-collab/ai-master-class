daily_steps = [3200, 7100, 9800, 10500, 6400, 11200]
target = 10000

for steps in daily_steps:
    print(f"Checking: {steps} steps")
    if steps >= target:
        print(f"Target hit on this day: {steps} steps. Stopping search.")
        break
    daily_steps = [3200, 7100, 9800, 4100, 10500, 6400]
minimum = 7000

total = 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum:
        print(f"Skipping {steps} (below minimum)")
        continue   # skip this day, go to next
    total += steps
    valid_days += 1

print(f"\nValid days: {valid_days}")
print(f"Total steps (valid days): {total}")
print(f"Average: {total // valid_days}")
fasting = "Autophagy Marathon"
cold_shower = True

# Write your if/elif/else logic below
# Change these values and run to see your score
steps         = 9200
water_glasses = 8
cold_shower   = True
fasting       = "OMAD"    # "OMAD", "2MAD", "Autophagy Marathon" or "None"
workout       = True

print("=== DAILY DISCIPLINE CHECK ===")
print()
# Create variables for your name, age, and city
# Print each one using an f-string
name = ""
age = 0
city = ""
print(f"My name is {name}, I am {age}, from {city}.")
# Write a program that takes a score and prints a grade
# 90+ = A, 75+ = B, 60+ = C, below 60 = F
score = 78
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
    daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD FAST", "workout"]
    print(daily_habits)
    daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
    print(daily_habits[0]) # First item
    print(daily_habits[2]) #Third item
    print(daily_habits[4]) #Last item
    weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400,10200]
    print("Last day:", weekly_steps[-1])
    print("Second to last:", weekly_steps[-2])
    print("First day:", weekly_steps[-7])
weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print("Days tracked:", len(weekly_steps))
daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
for habit in daily_habits:
    print("Habit:", habit)
    weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]

for steps in weekly_steps:
    if steps >= 10000:
        print(steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print(steps, "steps - Goal hit")
    else:
        print(steps, "steps - Below goal")
        skills_learned = ["welding", "tiling", "copywriting", "phone repair"]

if "welding" in skills_learned:
    print("Welding is in the list.")

if "beekeeping" not in skills_learned:
    print("Beekeeping not found. Add it to the list.")
    fasting_protocols = ["OMAD", "2MAD", "16:8", "Autophagy Marathon"]
print("Before:", fasting_protocols)
week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

for steps in week_steps:
    if steps >= 8000:
        print(steps, "- Goal hit")
    else:
        print(steps, "- Below goal")

print("Days tracked:", len(week_steps))
skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)
skills.append("phone repair")
print("After:", skills)

skills.append("graphic design")
print("Final:", skills)
skill = ["welding", "tiling", "upholstery"]
print("Before", skills)
# Insert "copywriting" at position 1 (second slot)
skills.insert(1, "copywriting")
print("After", skills)
habits = ["8 glasses water", "cold water", "OMAD FAST", "workout", "cold shower"]
print("Before:", habits)
habits.remove("cold shower") # Removes only the first one
print("After:", habits)
weekly_steps = [9200, 10500, 8800, 11000, 7600]
print("Before:", weekly_steps)

removed = weekly_steps.pop()   # Removes last item
print("Removed:", removed)
print("After:", weekly_steps)

removed2 = weekly_steps.pop(1) # Removes item at index 1
print("Removed:", removed2)
print("After:", weekly_steps)
weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print("Unsorted:", weekly_steps)

weekly_steps.sort()
print("Sorted low to high:", weekly_steps)

# Sort high to low by passing reverse=True
weekly_steps.sort(reverse=True)
print("Sorted high to low:", weekly_steps)
skills = ["welding", "tiling", "upholstery", "phone repair"]
skills.reverse()
print(skills)
habits = ["8 glasses water", "cold shower", "OMAD fast", "workout"]
position = habits.index("OMAD fast")
print("OMAD fast is at position:", position)
daily_results = ["hit", "miss", "hit", "hit", "miss", "hit", "hit"]
hit_count = daily_results.count("hit")
miss_count = daily_results.count("miss")
print("Days goal hit:", hit_count)
print("Days missed:", miss_count)
steps = [8800, 6500, 11000, 9200, 7300]

steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True)

print("Final list:", steps)

# Count days over 9000
high_days = 0
for s in steps:
    if s >= 9000:
        high_days += 1
print("Days over 9000 steps:", high_days)
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

print(daily_log)
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5

}
print("Steps today:", daily_log["steps"])
print("Protocol:", daily_log["fasting_protocol"])
print("Cold shower:", daily_log["cold_shower"])
# Add a new key
daily_log["pages_read"] = 30
print("After adding pages_read", daily_log)
# Update an existing key
daily_log["steps"] = 10400
print("After updating steps:", daily_log)
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "fasting_protocol": "OMAD",
    "junk_entry": "delete me"
}

del daily_log["junk_entry"]
print(daily_log)
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "fasting_protocol": "OMAD"
}

if "steps" in daily_log:
    print("Steps recorded:", daily_log["steps"])

if "sleep_hours" not in daily_log:
    print("Sleep hours not logged yet.")
    daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Loop through keys and values together
for key, value in daily_log.items():
    print(key, ":", value)
    client = {
        "name": "James",
         "weight_kg": 84.5,
         "goal": "fat loss",
         "fasting_protocol": "2MAD",
         "bench_press_kg": 80,
         "weekly_sessions": 4
    }
    print("Client profile:")
    for key, value in client.items():
        print(f" {key}: {value}")

        print()
        