f = open("Day2.txt")
open = [(op_choice, rec_choice) for op_choice, rec_choice in open.split('\n')]



Moves = {
    'A':1,
    'B':2,
    'C':3
}
total_score = 0

for op_choice, rec_choice in open:
    Moves = Moves[open]

    if op_choice == rec_choice:
        total_score += 3
    elif (op_choice == 'A' and rec_choice == 'C') or (op_choice == 'B' and rec_choice == 'A') or (op_choice == 'C' and rec_choice == 'B'):
        total_score += 6
    else:
        pass

print(total_score)

