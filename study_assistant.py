print("===== PERSONAL STUDY ASSISTANT =====")

name = input("Enter your name: ")

daily_hours = float(input("How many hours do you study daily? "))
target_hours = float(input("What is your daily study target (hours)? "))

weekly_hours = daily_hours * 7
weekly_target = target_hours * 7

print("\n===== YOUR STUDY REPORT =====")
print("Student:", name)
print("Daily study time:", daily_hours, "hours")
print("Weekly study time:", weekly_hours, "hours")

if daily_hours >= target_hours:
    print("Excellent! You achieved your daily study target.")
else:
    deficit = target_hours - daily_hours
    print("You are", deficit, "hours behind your daily target.")
    print("Keep practicing. You can improve!")

print("\nWeekly target:", weekly_target, "hours")
print("Keep learning and stay consistent!")
