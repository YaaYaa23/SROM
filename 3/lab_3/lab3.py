def num_arr(number):
    return [int(bit) for bit in reversed(str(number))] if number != 0 else [0]

def num_str(number):
    return ''.join(map(str, reversed(number))) if number != 0 else '0'

def equal_length(A, B):
    delta = len(A) - len(B)
    if delta > 0:
        B.extend([0] * delta)
    elif delta < 0:
        A.extend([0] * abs(delta))
    return A, B

def pop_null(number):
    while number and number[-1] == 0:
        number.pop()
    return number if number else [0]

def sub_pol(A, B):
    A, B = equal_length(A, B)
    result = [(a - b) % 2 for a, b in zip(A, B)]
    return mod_pol(result)

def add_pol(A, B):
    A, B = equal_length(A, B)
    result = [(a + b) % 2 for a, b in zip(A, B)]
    return mod_pol(result)
