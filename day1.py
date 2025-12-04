"""
Approach: parse out the moves, determine the position after each move,
check if the current position is zero, and if so, increment the counter 
"""
with open("day1_input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

start = 50

total = start

results = []

zero_counter = 0

for move in data:
    if move[0] == 'R':
        total = (total + int(move[1:])) % 100
    elif move[0] == 'L':
        total = (total - int(move[1:])) % 100
    
    results.append(total)

    if total == 0:
        zero_counter += 1

print(len(data))
print(zero_counter)

# first_move = 'R41'

# if first_move[0] == 'R':
#     total = start + int(first_move[1:])
# elif first_move[0] == 'L':
#     total = start - int(first_move[1:])

# second_move = 'R17'

# if second_move[0] == 'R':
#     total = (total + int(second_move[1:])) % 100
# elif second_move[0] == 'L':
#     total = (total - int(second_move[1:])) % 100

# print(total)