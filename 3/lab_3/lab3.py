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

def inverse(variable):
    result = variable
    for _ in range(0, 191 - 2):
        variable = mod_pol(sqr_pol(variable))
        result = mod_pol(mull_pol(result, variable))
    return mod_pol(sqr_pol(result))

def trace(variable):
    result = variable
    for i in range(0, 191 - 1):
        variable = mod_pol(sqr_pol(variable))
        result = mod_pol(add_pol(result, variable))

    return result

#A = '100101010101010101'
A = '10101101010101111010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
#B = '1010101011001'
B = '01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'
#C = '10101010000110101'
C = '01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'

A = num_arr(A)
B = num_arr(B)
C = num_arr(C)


print('Пункт А:\n')
res = num_str(add_pol(A, B))
print('\nA + B = ', res)
res = num_str(sub_pol(A, B))
print('\nA - B = ', res)
res = num_str(mull_pol(A, B))
print('\nA * B = ', res)
q, r = div_pol(A, B)
print('\nA // B = ', num_str(q))
print('\nA % B = ', num_str(r))
res = num_str(sqr_pol(A))
print('\nA^2 = ', res)
res = num_str(pow_pol(A, C))
print('\nA^C = ', res)
res = num_str(inverse(A))
print('\nA^-1 = ', res)
res = num_str(trace(A))
print('\ntrace(A) = ', res)
res = num_str(trace(B))
print('\ntrace(B) = ', res)





print('Пункт Б):\n')
res1 = num_str(mull_pol(add_pol(A, B), C))
print('(a+b)*с = ', res1)
res2 = num_str(add_pol(mull_pol(A, C), mull_pol(B, C)))
print('(a*с + c*b) = ', res2)
if res1 == res2:
    print('\nВиконується\n')
else:
    print('Помилка')





print('\nДодавання:')
cProfile.run('add_pol(A, B)')
print('\nВіднімання:')
cProfile.run('sub_pol(A, B)')
print('\nМноження:')
cProfile.run('mull_pol(A, B)')
print('\nДілення:')
cProfile.run('div_pol(A, B)')
print('\nСлід:')
cProfile.run('trace(A)')
print('\nПіднесення до квадрату:')
cProfile.run('sqr_pol(A)')
print('\nПіднесення до степення:')
cProfile.run('pow_pol(A, C)')
print('\nЗнаходження оберненого:')
cProfile.run('inverse(A)')
print('\n')
