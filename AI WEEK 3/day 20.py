weekly_steps = [9200, 7500, 10500, 8800, 6900, 1100, 9600]

goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
        print(goal_days)
weekly_steps = [9200, 7500, 10500, 8800, 6900, 1100, 9600]
goal_days = [steps for steps in weekly_steps if steps >= 8000]
print(goal_days)
clients = [
    {"name": "James",   "goal": "fat loss",    "sessions": 4},
    {"name": "Mwangi",  "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra",  "goal": "endurance",   "sessions": 3},
    {"name": "Patrick", "goal": "fat loss",    "sessions": 4},
    {"name": "Grace",   "goal": "fat loss",    "sessions": 3},
]

# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat loss clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print("Active clients:", [c["name"] for c in active_clients])
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

for i, status in enumerate(statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")