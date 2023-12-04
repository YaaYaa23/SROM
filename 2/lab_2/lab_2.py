import cProfile
import time


"""def create_num_from_hex(hex):
    hex = hex.lstrip('0x')
    num = []
    hex = (512 - len(hex)) * '0' + hex
    for i in range(65):
        num.append(int(hex[504 - 8 * i:512 - 8 * i], 16))
    return num"""
def create_num_from_hex(hex):
    hex = hex.lstrip('0x')
    num = []
    hex = (520 - len(hex)) * '0' + hex
    for i in range(65):
        num.append(int(hex[512 - 8 * i:520 - 8 * i], 16))
    return num

def convert_to_hex(num):
    result = ""
    for i in range(64, -1, -1):
        t = hex(num[i])[2:]
        if len(t) == 8:
            result += t
        else:
            t = hex(num[i])[2:]
            while len(t) != 8:
                t = '0' + t
            result += t
    return result
def convert_to_hex1(num):
    result = ""
    for i in range(64, -1, -1):
        t = hex(num[i])[2:]
        if len(t) == 8:
            result += t
        else:
            t = hex(num[i])[2:]
            while len(t) != 8:
                t = '0' + t
            result += t
    return result


def long_add(a, b):
    carry = 0
    c = [0] * 65
    for i in range(65):
        t = a[i] + b[i] + carry
        c[i] = t & 4294967295
        carry = t >> 32
    return c


def long_sub(a, b):
    borrow = 0
    c = [0] * 65
    if compare(a, b) == 1:
        for i in range(65):
            t = a[i] - b[i] - borrow
            if t >= 0:
                c[i] = t
                borrow = 0
            else:
                c[i] = 4294967296 + t
                borrow = 1
    else:
        for i in range(65):
            t = b[i] - a[i] - borrow
            if t >= 0:
                c[i] = t
                borrow = 0
            else:
                c[i] = 4294967296 + t
                borrow = 1
    #if borrow != 0:
        #print('Віднімання від меншого більше')
    return c
"""def long_sub(a, b):
    borrow = 0
    c = [0] * 256
    n = int(bit_length(a))
    for i in range(n+1):
        t = a[i] - b[i] - borrow
        if t >= 0:
            c[i] = t
            borrow = 0
        else:
            c[i] = 65536 + t
            borrow = 1
    if borrow != 0:
        print('Віднімання від меншого більше')
    return c"""


"""def long_mul_one_digit(a, digit):
    carry = 0
    c = [0] * 256
    for i in range(256):
        t = a[i] * digit + carry
        c[i] = t & 65535
        carry = t >> 16
    c.append(carry)
    return c"""
def long_mul_one_digit(a, digit):
    carry = 0
    c = [0] * 65
    n = int(bit_length(a))
    for i in range(n+1):
        t = a[i] * digit + carry
        c[i] = t & 4294967295
        carry = t >> 32
    #c.append(carry)
    c[n+1] = carry
    return c


def long_shift_bits_to_high(t, i):
    k = t
    for _ in range(i):
        k.insert(0, 0)  
        k.pop()  
    return k


"""def long_mul(a, b):
    c = [0] * 256
    for i in range(256):
        t = long_mul_one_digit(a, b[i])
        t = long_shift_bits_to_high(t, i)
        c = long_add(c, t)
    return c"""
def long_mul(a, b):
    c = [0] * 65
    n = int(bit_length(a))
    for i in range(n+1):
        t = long_mul_one_digit(a, b[i])
        #print(t)
        t = long_shift_bits_to_high(t, i)
        c = long_add(c, t)
    return c


def long_div_mod(A, B):
    k = bit_length(B)
    R = A
    Q = [0] * 65
    m = 0
    
    while compare(R, B) >= 0:
        t = bit_length(R)
        C = long_shift_bits_to_high(B, t - k)

        if compare(R, C) < 0:
            t = t - 1
            C = long_shift_bits_to_high(B, t - k)
        
        R = long_sub(R, C)
        m = m - 1
        Q[t-k] += 1
        
    
    return Q, R


"""def bit_length(num):
    for i in range(255, -1, -1):
        if num[i] != 0:
            return i"""

def bit_length(num):
    for i in range(64, -1, -1):
        if num[i] != 0:
            return i
    return 0


def compare(num1, num2):
    for i in range(64, -1, -1):
        if num1[i] < num2[i]:
            return -1
        elif num1[i] > num2[i]:
            return 1
    return 0

def convert_to_bin(coef):
    res = ""
    for i in range(64, -1, -1):
        t = bin(coef[i])[2:]
        if len(t) == 32:
            res += t
        else:
            t = bin(coef[i])[2:]
            while len(t) != 32:
                t = '0' + t
            res += t
    return res


def LongPowerWindow(base, exp):
    c = [1] + [0] * 64
    t = convert_to_bin(exp)[::-1]
    for i in range(bit_length(t), -1, -1):
        if t[i] == '1':
            c = long_mul(c, base)
        if i != 0:
            c = long_mul(c, c)
    return c


def euclidean_algorithm(a, b):
    while a[0]:
        result = long_div_mod(a, b)
        if result[0] is not None and result[1] is not None:
            a, b = result[1], a
        #print(result)
        #print("\nA",a)
        #print("\nB",b)
    return result[0]

def lcm(a, b):
    gcd = euclidean_algorithm(a, b)
    c = long_mul(a, b)
    #print("\ngcd",gcd)
    c = int(convert_to_hex(c).lstrip('0'), 16)
    gcd = int(convert_to_hex(gcd).lstrip('0'), 16)
    #lcm = long_div_mod(c, gcd)  
    lcm = c // gcd
    lcm = hex(lcm)
    return lcm



def LongPowerWindow(base, exp):
    c = [1] + [0] * 63
    t = convert_to_bin(exp)[::-1]
    for i in range(bit_length(t), -1, -1):
        if t[i] == '1':
            c = long_mul(c, base)
        if i != 0:
            c = long_mul(c, c)
    return c


def calc(mod):
    k = bit_length(mod) + 1
    mod = int(convert_to_hex1(mod).lstrip('0x'), 16)
    #print(int('cbe75e23d145c3dc78d76739b63d337cc33268e08ce4ea7319c38b7d57b1747d59010759f3b015858dc5a9d5ddbbd3ef41a368ba1ca6d8a6d967f2fed6b7033e7f56d46beae7c259cce870e0879f49849c956b6b6810be90d0c50c54daaef41b2b1c6e3c7b2ed35da549a7c95fd551841ea90e4196e8272b42ea3dba7cdcef', 16))
    mu = ((2**32) ** (2*k)) // mod
    mu = create_num_from_hex(hex(mu).lstrip('0x'))
    return mu, k
    
"""def kill_last(A, k):
    A = A[k:]
    A.extend([0 for i in range(k)])
    #A[0] = A[0]//(2**16)
    #A = convert_to_hex(A).lstrip('0x')
    #A = create_num_from_hex(A)
    return A"""
def kill_last(A, k):
    A = convert_to_hex(A)
    A = int(A, 16)
    A = hex(A // (2**k))
    A = create_num_from_hex(A)
    return A




def long_sub_abs(x, q):
    if compare(x, q) >= 0:
        return long_sub(x,q), 0
    return long_sub(q,x), 1

def barrett_reduction(x, n, mu, k):
    k = 1024
    res = 0
    #print('mu', convert_to_hex(mu).lstrip('0x'))
    #mu, k = calc_mu(n)
    #k = calc_mu(n)[1]
    q = kill_last(x, k - 1)
    #print("before",convert_to_hex(q).lstrip('0x'))
    q = long_mul(mu, q)
    #print(convert_to_hex1(q).lstrip('0x'))
    q = kill_last(q, k + 1)
    q = long_mul(n, q) 
    r, sign = long_sub_abs(x, q)
    #print(convert_to_hex(x).lstrip('0x'))
    #print(convert_to_hex(n).lstrip('0x'))
    if sign == 1:
        #print(convert_to_hex(r))
        #print("hello")
        return long_sub(n,r)
    while compare(r, n) >= 0:
        r = long_sub(r, n)
        res = res + 1
    #print(res)
    return r

def long_add_mod(a, b, mod, mu, k):
    result = long_add(a, b)
    #i = 0
    while compare(result, mod) == 1:
        #i += 1
        result = long_sub(result, mod)
        #print(i)
    return result
    #return barrett_reduction(result, mod, mu, k)

def long_sub_mod(a, b, mod, mu, k):
    result = long_sub(a, b)
    #print("\nA-B=", convert_to_hex(result).lstrip('0'))
    while compare(result, mod) == 1:
        result = long_sub(result, mod)
    if compare(a, b) == -1:
        result = long_sub(mod, result)
    return result
    #return barrett_reduction(result, mod, mu, k)

def long_mul_mod(a, b, mod, mu, k):
    result = long_mul(a, b)
    #print(result)
    return barrett_reduction(result, mod, mu, k)

def long_mod_power_barrett( a, b, mod, mu, k):
    c = [1] + [0] * 64
    #t = convert_to_bin(b)[::-1]
    t = bin(int(b,16)).lstrip('0b')
    #print(t)
    #print(len(t))
    for i in range(len(t)-1, -1, -1):
        #print("i",i)
        if t[i] == '1':
            c = long_mul_mod(a, c, mod, mu, k)
            #print("c0",c)
        a = long_mul_mod( a, a, mod, mu, k)
        #print("c1",c)
        #if i != 0:
            #c = long_mul_mod(c, c, mod)
    return c

#A = 'd0a166bef0f8cd687a755ce64c4736e2621fe749af3c4170354c55a2728037612cf3b134550036e2de888e049ee782ab82ab99ba3442a3b4b8eb21c9f79778cff4ce0c2109a02fd18163e5155146d156b92176c03ba2b87ee53ba78217529616eea6e8432b0f736b09e30e89f3ceeaea11fb94dacd994e1fd8a6059cc14a58b2'
A = 'a9694988354c96530b1a58f8ad59569af0d402ab53d275ddb5cb393f47c6b098977f181ab889d3c5ceb96b9f3c0702c947856481d654c691d0f736fa2ef7aa0fbec62224e467f741e53edf8c8fe82c13fb90ac66eee37a975f16dd9faafd213c538711bbea34fbfd8b4330e17409d5c35313743d5dea5a82d34d99a10ac9223b'
#mod = 'cbe75e23d145c3dc78d76739b63d337cc33268e08ce4ea7319c38b7d057b1747d59010759f3b015858dc5a9d05ddbbd3ef41a368ba1ca6d8a6d967f2fed6b7033e7f56d46beae7c259cce870e0879f49849c956b6b6810be90d0c50c54daaef41b2b1c6e3c7b2ed35da549a7c95fd551841ea90e4196e8272b42ea3dba7cdcef'
mod = 'cbe75e23d145c3dc78d76739b63d337cc33268e08ce4ea7319c38b7d057b1747d59010759f3b015858dc5a9d05ddbbd3ef41a368ba1ca6d8a6d967f2fed6b7033e7f56d46beae7c259cce870e0879f49849c956b6b6810be90d0c50c54daaef41b2b1c6e3c7b2ed35da549a7c95fd551841ea90e4196e8272b42ea3dba7cdcef'
B = 'd0a166bef0f8cd687a755ce64c4736e2621fe749af3c4170354c55a2728037612cf3b134550036e2de888e049ee782ab82ab99ba3442a3b4b8eb21c9f79778cff4ce0c2109a02fd18163e5155146d156b92176c03ba2b87ee53ba78217529616eea6e8432b0f736b09e30e89f3ceeaea11fb94dacd994e1fd8a6059cc14a58b2'
#B = 'a9694988354c96530b1a58f8ad59569af0d402ab53d275ddb5cb393f47c6b098977f181ab889d3c5ceb96b9f3c0702c947856481d654c691d0f736fa2ef7aa0fbec62224e467f741e53edf8c8fe82c13fb90ac66eee37a975f16dd9faafd213c538711bbea34fbfd8b4330e17409d5c35313743d5dea5a82d34d99a10ac9223b'
E = '3A7EF2554E8940FA9B93B2A5E822CC7BB262F4A14159E4318CAE3ABF5AEB1022EC6D01DEFAB48B528868679D649B445A753684C13F6C3ADBAB059D635A2882090FC166EA9F0AAACD16A062149E4A0952F7FAAB14A0E9D3CB0BE9200DBD3B0342496421826919148E617AF1DB66978B1FCD28F8408506B79979CCBCC7F7E5FDE7'
F = 'd0a166bef0f8cd687a755ce64c4736e2621fe749af3c4170354c55a2728037612cf3b134550036e2de888e049ee782ab82ab99ba3442a3b4b8eb21c9f79778cff4ce0c2109a02fd18163e5155146d156b92176c03ba2b87ee53ba78217529616eea6e8432b0f736b09e30e89f3ceeaea11fb94dacd994e1fd8a6059cc14a58b2'

A = create_num_from_hex(A)
B = create_num_from_hex(B)
mod = create_num_from_hex(mod)
E = create_num_from_hex(E)
mu, k = calc(mod)


D = long_add(A, B)
print("\nA+B=", convert_to_hex(D).lstrip('0'))
D = long_sub(A, B)
print("\nA-B=", convert_to_hex(D).lstrip('0'))
D = long_mul(A, B)
print("\nA*B=", convert_to_hex1(D).lstrip('0'))

C = euclidean_algorithm(A, B)
print("\nAgcdB=", convert_to_hex(C).lstrip('0'))
C = lcm(A, B)
print("\nAlcmB=", C.lstrip('0x'))#convert_to_hex(C).lstrip('0'))
#D = barrett_reduction(A, B, mu, k)
#print("\nAmodB=", convert_to_hex(D).lstrip('0'))
D = long_add_mod(A, B, mod, mu, k)
print("\nA+BmodA=", convert_to_hex(D).lstrip('0'))
D = long_sub_mod(A, B, mod, mu, k)
print("\nA-BmodA=", convert_to_hex(D).lstrip('0'))
D = long_mul_mod(A, B, mod, mu, k)
print("\nA*BmodM=", convert_to_hex(D).lstrip('0'))
start = time.time()
D = long_mod_power_barrett(A, F, mod, mu, k)
print("\n1A**BmodM=", convert_to_hex(D).lstrip('0'))
end = time.time()
execution_time = end - start
print(f"1Час виконання функції: {execution_time} секунд")


print('Б1):')
res1 = long_mul_mod(long_add_mod(A, B, mod, mu, k), E, mod, mu, k)
print('(a+b)*с (mod n) = ', convert_to_hex(res1).lstrip('0'))
res2 = long_mul_mod(E, long_add_mod(A, B, mod, mu, k), mod, mu, k)
print('c*(a+b) (mod n) = ', convert_to_hex(res2).lstrip('0'))
res3 = long_add_mod(long_mul_mod(A, E, mod, mu, k), long_mul_mod(B, E, mod, mu, k), mod, mu, k)
print('a*c + b*c (mod n) = ', convert_to_hex(res3).lstrip('0'))

if res1 == res2 and res2 == res3:
    print('\nВиконується')
else:
    print('\nНе виконується')

print('Б2):')
N = '65'
N = create_num_from_hex(N)
res4 = long_mul_mod(A, N, mod, mu, k)
print('n*a modm)))))) = ', convert_to_hex(res4).lstrip('0'))
res5 = '0'
res5 = create_num_from_hex(res5)
for i in range(101):
    res5 = long_add_mod(res5, A, mod, mu, k)
    # print('res5 = ', res5)
print('(a+...+a)modm) = ', convert_to_hex(res5).lstrip('0'))
if res4 == res5:
    print('\nВиконується')
else:
    print('\nНе виконується')


print('\nВ:')
print('\ngcd')
c = cProfile.run('euclidean_algorithm(A, B)')
print("c",c)
print('\nlcm')
cProfile.run('lcm(A, B)')
print('\nBarrettReduction')
cProfile.run('barrett_reduction(A, B, mu, k)')
print('\nAddmod')
cProfile.run('long_add_mod(A, B, mod, mu, k)')
print('\nSubmod')
cProfile.run('long_sub_mod(A, B, mod, mu, k)')
print('\nMulmod')
cProfile.run('long_mul_mod(A, B, mod, mu, k)')
print('\nLongPowermod')
cProfile.run('long_mod_power_barrett(A, F, mod, mu, k)')
