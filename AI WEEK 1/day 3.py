# Day 3 Workout Session Report

# Workout data
number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60  # kg
session_duration = 45  # minutes

# Calculations
total_sets = number_of_exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume = total_reps * average_weight_per_rep
reps_per_minute = total_reps / session_duration
volume_exceeded = total_volume > 10000

# Session report
print("Day 3 Workout Session Report")
print("-----------------------------")
print(f"Total sets: {total_sets}")
print(f"Total reps: {total_reps}")
print(f"Total volume: {total_volume} kg")
print(f"Reps per minute: {reps_per_minute:.2f}")
print(f"Volume exceeded 10,000 kg: {volume_exceeded}")
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
  # Print the first 10 even numbers using a loop
for i in range(1, 21):
    if i % 2 == 0:
        print(i)  