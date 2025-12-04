with open("day2.txt") as f:
    ranges = f.read().split(',')

print(ranges)

def valid_id(number: int):
    """
    Return True if the id is invalid
    """
    n_str = str(number)
    length = len(n_str)
    if length % 2 == 0:
        first_half = n_str[:len(n_str) // 2]
        second_half = n_str[len(n_str) // 2:]
    
        return first_half != second_half
    else:
        return True
        
invalid_sum = 0

for r in ranges:
    range_split = r.split('-')
    numbers = range(int(range_split[0]), int(range_split[1])+1)
    for n in numbers:
        if not valid_id(n):
            invalid_sum += n

print(invalid_sum)
