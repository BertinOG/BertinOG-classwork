f = open("Day2.txt")
contents = f.read()
opened = [(op_choice, rec_choice) for op_choice, rec_choice in contents.split('\n') if op_choice and rec_choice]
Moves = {
    'A':1,
    'B':2,
    'C':3
}
total_score = 0
for op_choice, rec_choice in opened:
    if op_choice == rec_choice:
        total_score += 3
    elif (op_choice == 'A' and rec_choice == 'C') or (op_choice == 'B' and rec_choice == 'A') or (op_choice == 'C' and rec_choice == 'B'):
        total_score += 6
print(total_score)
