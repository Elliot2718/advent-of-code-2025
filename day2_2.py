with open("day2.txt") as f:
    ranges = f.read().split(',')

print(ranges)

def valid_id(number: int):
    """
    Return True if the id is invalid
    """
    is_valid = True
    n_str = str(number)
    length = len(n_str)
    max_check_length = length // 2
    for check_length in range(1, max_check_length+1):
        if length % check_length == 0:
            check_number = n_str[:check_length] * (length // check_length)
            # print(f"{n_str[:check_length]} {check_number} {number} {int(check_number) != number}")
            is_valid = is_valid and (int(check_number) != number)

    return is_valid
        
invalid_sum = 0

for r in ranges:
    range_split = r.split('-')
    numbers = range(int(range_split[0]), int(range_split[1])+1)
    for n in numbers:
        if not valid_id(n):
            invalid_sum += n

# r = '211000-212300'
# range_split = r.split('-')
# numbers = range(int(range_split[0]), int(range_split[1])+1)
# for n in numbers:
#     if not valid_id(n):
#         invalid_sum += n

print(invalid_sum)
