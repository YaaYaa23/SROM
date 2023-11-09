A = 'd0a166bef0f8cd687a755ce64c4736e2621fe749af3c4170354c55a2728037612cf3b134550036e2de888e049ee782ab82ab99ba3442a3b4b8eb21c9f79778cff4ce0c2109a02fd18163e5155146d156b92176c03ba2b87ee53ba78217529616eea6e8432b0f736b09e30e89f3ceeaea11fb94dacd994e1fd8a6059cc14a58b2'
mod = 'cbe75e23d145c3dc78d76739b63d337cc33268e08ce4ea7319c38b7d057b1747d59010759f3b015858dc5a9d05ddbbd3ef41a368ba1ca6d8a6d967f2fed6b7033e7f56d46beae7c259cce870e0879f49849c956b6b6810be90d0c50c54daaef41b2b1c6e3c7b2ed35da549a7c95fd551841ea90e4196e8272b42ea3dba7cdcef'
B = 'a9694988354c96530b1a58f8ad59569af0d402ab53d275ddb5cb393f47c6b098977f181ab889d3c5ceb96b9f3c0702c947856481d654c691d0f736fa2ef7aa0fbec62224e467f741e53edf8c8fe82c13fb90ac66eee37a975f16dd9faafd213c538711bbea34fbfd8b4330e17409d5c35313743d5dea5a82d34d99a10ac9223b'


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
            c[i] = 65536 + t
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

C = euclidean_algorithm(A, B)
print("\nAgcdB=", convert_to_hex(C).lstrip('0'))
C = lcm(A, B)
print("\nAlcmB=", C.lstrip('0x'))#convert_to_hex(C).lstrip('0'))
