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

def create_matrix(m):
    result = []
    p = 2 * m + 1

    for i in range(m):
        result.append([1 if (2 ** i + 2 ** j) % p == 1 or
                           (2 ** i - 2 ** j) % p == 1 or
                           (-2 ** i + 2 ** j) % p == 1 or
                           (-2 ** i - 2 ** j) % p == 1 else 0
                       for j in range(m)])

    return result

def mull_matrix(pol1, pol2):
    pol21 = len(pol2) if isinstance(pol2[0], list) else 1
    pol11 = len(pol1)
    res = []
    for i in range(pol21):
        total_sum = 0
        for j in range(pol11):
            if pol21 == 1:
                total_sum += pol1[j] * pol2[j]
            else:
                total_sum += pol1[j] * pol2[i][j]
        res.append(total_sum % 2)

    return res

def mull_pol(pol1, pol2):
    matr = create_matrix(191)
    res = []
    for i in range(191):
        pol1i = move_left(pol1.copy(), i)
        pol1_matr = mull_matrix(pol1i, matr)
        pol2i = move_left(pol2.copy(), i)
        pol1_matr = mull_matrix(pol1_matr, pol2i)
        res.append(pol1_matr[0])

    return res

def trace(pol):
    result = 0
    for i in pol:
        result += i

    result %= 2
    return result
