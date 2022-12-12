f = open("Day1.txt")
lines = f.read().strip().split("\n")

calories = {}
current_elf = 1

for line in lines:
    if not line:
        current_elf += 1
    else:
        calories[current_elf] = calories.get(current_elf, 0) + int(line)

sorted_elves = sorted(calories, key=calories.get, reverse=True)

total_calories = 0

for elf in sorted_elves[:3]:
    total_calories += calories[elf]

print(f"The top 3 elves are carrying a total of {total_calories} calories")