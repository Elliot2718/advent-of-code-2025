def zero_counter(start, move):
    """
    example: start at 1, move is R10, output 11
    """
    if move[0] == 'L':
        start = (100 - start) % 100 # flip it
    
    result = start + int(move[1:])
    return result // 100

def next_position(start, move):
    if move[0] == 'R':
        result = start + int(move[1:])
    elif move[0] == 'L':
        result = start - int(move[1:])

    return result % 100

test_cases = [
    (1, 'R10', 11, 0),
    (1, 'L10', 91, 1),
    (0, 'R10', 10, 0),
    (0, 'L10', 90, 0),
    (99, 'R10', 9, 1),
    (99, 'L10', 89, 0),
    (1, 'R200', 1, 2),
    (1, 'L200', 1, 2),
    (0, 'R200', 0, 2),
    (0, 'L200', 0, 2),
    (99, 'R101', 0, 2),
    (1, 'L101', 0, 2),
]

for test in test_cases:
    start = test[0]
    move = test[1]
    zeros = zero_counter(start, move)
    end = next_position(start, move)
    correct_end = end == test[2]
    correct_zeros = zeros == test[3]
    print(f"{start} {move} {zeros} {end} {correct_end} {correct_zeros}")



with open("day1_input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

position = 50
zeros = 0

for move in data:
    zeros += zero_counter(position, move)
    position = next_position(position, move)

print(zeros)


#     if result % 100 == 0:
#         zero_counter += 1
#     if prior_total == 0 and (result < 0 or result >= 100):
#         zero_counter -= 1
#     zero_counter += abs(result // 100)


#     total = result % 100

#     results.append(result)
#     zeros.append(zero_counter)
#     totals.append(total)
#     prior_total = total

# for a, b, c, d in list(zip(data, results, zeros, totals))[:100]:
#     print(f"{a:>6} {b:>6} {c:>6} {d:>6}")

# print(zero_counter)

# moves = [int(d[1:]) for d in data]
# moves.sort()
# print(moves)

# 6364 is too high

