import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# STEP 1: Historical SMP fitness data
data = {
    "sleep": [
        6.5, 7.2, 5.8, 8.0, 6.0, 7.5, 8.2,
        5.5, 7.0, 6.8, 8.5, 6.2, 7.8, 5.9,
        7.1, 8.0, 6.4, 7.6, 5.7, 8.3, 6.9,
        7.4, 6.1, 8.1, 5.8, 7.7, 6.6, 7.9
    ],
    "water": [
        2, 3, 1.5, 3, 2, 2.5, 3,
        1.5, 2.5, 2, 3, 1.5, 2.5, 2,
        3, 2.5, 2, 3, 1.5, 3, 2.5,
        2, 1.5, 3, 2, 2.5, 2, 3
    ],
    "workout": [
        20, 40, 10, 45, 15, 35, 50,
        10, 30, 25, 50, 15, 40, 20,
        35, 45, 20, 40, 10, 50, 30,
        35, 15, 45, 20, 40, 25, 35
    ],
    "steps": [
        8500, 12000, 6500, 14000, 9000, 11000, 13500,
        6000, 10500, 9500, 15000, 7000, 12500, 8000,
        11500, 14500, 9000, 13000, 6500, 15500, 10000,
        12000, 7500, 14000, 8500, 12500, 9500, 11000
    ]
}

df = pd.DataFrame(data)

# The goal is reached when steps are at least 10,000
df["hit_goal"] = (df["steps"] >= 10000).astype(int)

X = df[["sleep", "water", "workout"]]
y = df["hit_goal"]

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(X, y)

accuracy = model.score(X, y)
print(f"Training accuracy: {accuracy:.2%}")
print("Step 1 complete: Classifier trained on 28 days.")
print("Training records:", len(df))


# STEP 2: Build the AI coaching response system
def coaching_message(sleep, water, workout, prediction):
    if prediction == 1:
        message = (
            "Your predicted result is reaching the 10,000-step goal. "
            "Keep moving consistently and maintain your routine."
        )
    else:
        message = (
            "You may need extra effort to reach 10,000 steps. "
            "Try a short walk and gradually increase your activity."
        )

    if sleep < 7:
        message += " Try to get more sleep if possible."

    if water < 2:
        message += " Remember to drink water regularly."

    if workout < 20:
        message += " Consider adding a short activity session."

    return message

print("Step 2 complete: Coaching system created.")


# STEP 3: Connect the classifier to the coaching system
def predict_and_coach(sleep, water, workout):
    new_day = pd.DataFrame([{
        "sleep": sleep,
        "water": water,
        "workout": workout
    }])

    prediction = int(model.predict(new_day)[0])

    result = "YES" if prediction == 1 else "NO"

    message = coaching_message(
        sleep, water, workout, prediction
    )

    return result, message

print("Step 3 complete: Prediction and coaching connected.")


# STEP 4: Test a batch of new days
new_days = [
    {"day": "Monday", "sleep": 8, "water": 3, "workout": 45},
    {"day": "Tuesday", "sleep": 5.5, "water": 1.5, "workout": 10},
    {"day": "Wednesday", "sleep": 7, "water": 2.5, "workout": 30},
    {"day": "Thursday", "sleep": 6, "water": 2, "workout": 15},
]

print("\nSMP PERFORMANCE COACH")
print("=" * 40)

for day in new_days:
    result, message = predict_and_coach(
        day["sleep"],
        day["water"],
        day["workout"]
    )

    print(f"\nDay: {day['day']}")
    print(f"Sleep: {day['sleep']} hours")
    print(f"Water: {day['water']} litres")
    print(f"Workout: {day['workout']} minutes")
    print(f"Predicted to hit 10,000 steps: {result}")
    print(f"Coach: {message}")

print("\nStep 4 complete: All days processed.")
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete data: sleep {sleep}h, water {water} glasses, "
              f"bench {bench}kg. "
              f"Goal prediction: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence). "
              "Give a 2-sentence coaching response. Be direct and specific.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": ("You are an SMP performance coach. "
                          "You give direct, data-driven coaching feedback. "
                          "No filler. Two sentences maximum.")},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content