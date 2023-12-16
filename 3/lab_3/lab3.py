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

def mull_pol(A, B):
    if A == 0 or B == 0:
        return 0
    A, B = equal_length(A, B)
    result = [0] * (2 * len(A))
    for i, a in enumerate(A):
        if a == 0:
            continue
        for j, b in enumerate(B):
            if b == 0:
                continue
            result[i + j] = (result[i + j] + a * b) % 2
    return mod_pol(result)

def mod_pol(number):
    ourMod = [0] * 192
    ourMod[191], ourMod[9], ourMod[0] = 1, 1, 1
    _, remainder = div_pol(number, ourMod)
    return remainder

def div_pol(A, B):
    A = pop_null(A)
    compare = cmp(A, B)
    if compare == 0:
        return [0], [0]
    if compare == -1:
        return [0], A

    k = len(B)
    r = A.copy()
    q = [0] * len(A)

    while cmp(r, B) != -1:
        t = len(r)
        c = append_null(B, t - k)
        r = sub_pol(r, c)
        q[t - k] = 1

    q = pop_null(q)
    r = pop_null(r)
    return q, r

def cmp(A, B):
    A = pop_null(A)
    B = pop_null(B)

    if A != 0:
        lenA = len(A)
    else:
        lenA = 0

    if B != 0:
        lenB = len(B)
    else:
        lenB = 0

    if lenA > lenB:
        return 1
    elif lenA < lenB:
        return -1
    else:
        for i in range(len(A) - 1, -1, -1):
            if A[i] == B[i]:
                pass
            elif A[i] > B[i]:
                return 1
            else:
                return -1

    return 0

def append_null(array, k):
    return [0] * k + array

def sqr_pol(variable):
    return mull_pol(variable, variable)

def pow_pol(variable, C):
    result = [0] * len(C)
    result[0] = 1
    for exp in C:
        if exp == 1:
            result = mull_pol(result, variable)
        variable = sqr_pol(variable)
    return result


