def check_steps(steps, goal=8000):
    if steps >= goal:
        print(f"{steps} steps - Goal of {goal} hit.")
    else:
        print(f"{steps} steps - Goal of {goal} missed.")

# Uses the default goal of 8000
check_steps(9200)
check_steps(7500)
def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")

log_day(9200)                        # Uses both defaults
log_day(10500, water=9)              # Override water only
log_day(8800, water=7, protocol="2MAD")  # Override both
def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"{name} | Goal: {goal} | Sessions/week: {sessions} | Bench: {bench_kg}kg")

# Positional arguments
client_report("James", "fat loss")

# Keyword arguments: order does not matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100)

# Mix of positional and keyword
client_report("Sandra", "endurance", bench_kg=50)
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Weight: {weight}kg | Height: {height}m")
print(f"BMI: {bmi} | Category: {category}")