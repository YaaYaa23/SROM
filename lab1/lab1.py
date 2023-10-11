import cProfile
D = 'DAF1ABDA4AD4D9FE3E36A529210C2AE99B905922FC0519798A26E351FE23AF375AD6BA288EE030B70DF0CE1CDF1E8B75BA56494DC6ED36B181814CD5783E6C81'
A = 'D4D2110984907B5625309D956521BAB4157B8B1ECE04043249A3D379AC112E5B9AF44E721E148D88A942744CF56A06B92D28A0DB950FE4CED2B41A0BD38BCE7D0BE1055CF5DE38F2A588C2C9A79A75011058C320A7B661C6CE1C36C7D870758307E5D2CF07D9B6E8D529779B6B2910DD17B6766A7EFEE215A98CAC300F2827DB'
B = '3A7EF2554E8940FA9B93B2A5E822CC7BB262F4A14159E4318CAE3ABF5AEB1022EC6D01DEFAB48B528868679D649B445A753684C13F6C3ADBAB059D635A2882090FC166EA9F0AAACD16A062149E4A0952F7FAAB14A0E9D3CB0BE9200DBD3B0342496421826919148E617AF1DB66978B1FCD28F8408506B79979CCBCC7F7E5FDE7'


def create_num_from_hex(hex):
    hex = hex.lstrip('0x')
    num = []
    hex = (1024 - len(hex)) * '0' + hex
    for i in range(256):
        num.append(int(hex[1020 - 4 * i:1024 - 4 * i], 16))
    return num


def convert_to_hex(num):
    result = ""
    for i in range(255, -1, -1):
        t = hex(num[i])[2:]
        if len(t) == 4:
            result += t
        else:
            t = hex(num[i])[2:]
            while len(t) != 4:
                t = '0' + t
            result += t
    return result


def long_add(a, b):
    carry = 0
    c = [0] * 256
    for i in range(256):
        t = a[i] + b[i] + carry
        c[i] = t & 65535
        carry = t >> 16
    return c


def long_sub(a, b):
    borrow = 0
    c = [0] * 256
    for i in range(256):
        t = a[i] - b[i] - borrow
        if t >= 0:
            c[i] = t
            borrow = 0
        else:
            c[i] = 65535 + t
            borrow = 1
    if borrow != 0:
        print('Віднімання від меншого більше')
    return c


def long_mul_one_digit(a, digit):
    carry = 0
    c = [0] * 256
    for i in range(256):
        t = a[i] * digit + carry
        c[i] = t & 65535
        carry = t >> 16
    c.append(carry)
    return c


def long_shift_bits_to_high(t, i):
    k = t
    for _ in range(i):
        k.insert(0, 0)  
        k.pop()  
    return k


def long_mul(a, b):
    c = [0] * 256
    for i in range(256):
        t = long_mul_one_digit(a, b[i])
        t = long_shift_bits_to_high(t, i)
        c = long_add(c, t)
    return c


def long_div_mod(A, B):
    k = bit_length(B)
    R = A
    Q = [0] * 256
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


def bit_length(num):
    for i in range(255, -1, -1):
        if num[i] != 0:
            return i


def compare(num1, num2):
    for i in range(255, -1, -1):
        if num1[i] < num2[i]:
            return -1
        elif num1[i] > num2[i]:
            return 1
    return 0

def convert_to_bin(coef):
    res = ""
    for i in range(255, -1, -1):
        t = bin(coef[i])[2:]
        if len(t) == 16:
            res += t
        else:
            t = bin(coef[i])[2:]
            while len(t) != 16:
                t = '0' + t
            res += t
    return res


def LongPowerWindow(base, exp):
    c = [1] + [0] * 255
    #t = convert_to_bin(exp)[::-1][:bit_length(exp)]
    t = convert_to_bin(exp)[::-1]
    for i in range(bit_length(t), -1, -1):
        if t[i] == '1':
            c = long_mul(c, base)
        if i != 0:
            c = long_mul(c, c)
    return c

M = '37'
O = '0'
O = create_num_from_hex(O)
print("\nO", O)
M = create_num_from_hex(M)
A = create_num_from_hex(A)
B = create_num_from_hex(B)
C = long_add(A, B)
print("\nA+B=", convert_to_hex(C).lstrip('0'))
C = long_sub(A, B)
print("\nA-B=", convert_to_hex(C).lstrip('0'))
C = long_mul_one_digit(C, int(3))
print("\nA*3=", convert_to_hex(C).lstrip('0'))
C = long_mul(A, B)
print("\nA*B=", convert_to_hex(C).lstrip('0'))
Q, R = long_div_mod(A, B)
print("\nA/B =", convert_to_hex(Q).lstrip('0'))
print("\nR =", convert_to_hex(R).lstrip('0'))
C = LongPowerWindow(A, B)
print("\nA**B=", convert_to_hex(C).lstrip('0'))
C = compare(A, B)
if C == 1:
    print("\nA > B")
elif C == 0:
    print("\nA = B")
else:
    print("\nA < B")
D = create_num_from_hex(D)


print('Б1:')
res1 = long_mul(long_add(A, B), D)
print('\n(a + b)*c = ', convert_to_hex(res1).lstrip('0'))
res2 = long_mul(D, long_add(A, B))
print('\nc*(a + b) = ', convert_to_hex(res2).lstrip('0'))
res3 = long_add(long_mul(A, D), long_mul(B, D))
print('\na*c + b*c = ', convert_to_hex(res3).lstrip('0'))

if res1 == res2 and res2 == res3:
    print('\nВиконується')
else:
    print('\nНе виконується')
print('Б2:')
res4 = long_mul(M, A)
print('\nM*A = ', convert_to_hex(res4).lstrip('0'))
print(len(res4))
res5 = [0] * 256
for i in range(55):
    res5 = long_add(res5, A)
print('\nA+A+...A+A (M-разів)= ', convert_to_hex(res5).lstrip('0'))
if res4 == res5:
    print('\nВиконуєьтся')
else:
    print('\nНе виконуєьтся')



print('\nВ:')
print('\nAdd')
cProfile.run('long_add(A, B)')
print('\nSub')
cProfile.run('long_sub(A, B)')
print('\nMul')
cProfile.run('long_mul(A, B)')
print('\nDiv')
cProfile.run('long_div_mod(A,B)')
print('\nLongPower')
cProfile.run('LongPowerWindow(A, B)')