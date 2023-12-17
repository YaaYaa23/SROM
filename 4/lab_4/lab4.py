import cProfile

def num_arr(number):
    return [int(bit) for bit in str(number)] if number != 0 else [0]

def num_str(number):
    return ''.join(map(str, number)) if number != 0 else '0'

def equal_length(A, B):
    delta = len(A) - len(B)
    if delta > 0:
        B.extend([0] * delta)
    elif delta < 0:
        A.extend([0] * abs(delta))
    return A, B

def move_left(number, m):
    m = m % len(number)  
    return number[m:] + number[:m]

def move_right(number, m):
    m = m % len(number)  
    return number[-m:] + number[:-m]

def add_pol(A, B):
    A, B = equal_length(A, B)
    result = [(a + b) % 2 for a, b in zip(A, B)]
    return result
