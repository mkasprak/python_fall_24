# Tracking blood sugar
# by day
# and by meal
total = 0
average = 0

times_of_day = ["Breakfast", "Lunch", "Dinner", "Bedtime"]
blood_sugar_levels = []
for time in times_of_day:
    level = input(f"Enter your blood sugar level for {time}: ")
    blood_sugar_levels.append([time, level])

print(blood_sugar_levels)
for i in range(4):
    time = blood_sugar_levels[i][0]
    level = blood_sugar_levels[i][1]
    total += int(level)
    print(f"At {time} your blood sugar level was: {level}")

average = total/4
print(f"Your average blood sugar today was: {average:.0f}")
