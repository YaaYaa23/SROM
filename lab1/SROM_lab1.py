import cProfile
A = str(int('0x2214c7ad0d81ce96e2673abbdf3fbb8e18c6259f632a88002f3d662e9449878e2ba1d324c8d8008d8836832be433b097adfc87069568ea7cc9eb9f2a1e58d31cff07e79c95b4e38963ba182d42541aeb8617860301b3237ef08cc5ae86cd5c902fa06c5327b028969ceba1700124616f52a35f8a7e7e0a9f0beffbda05d08a7dd', 16))
B = str(int('0x1694d7ad0d81ce96e2673abbdf3fbb8e18c6259f632a88002f3d662e9449878e2ba1d324c8d8008d8836832be433b097adfc87069568ea7cc9eb9f2a1e58d31cff07e79c95b4e38963ba182d42541aeb8617860301b3237ef08cc5ae86cd5c902fa06c5327b028969ceba1700124616f52a35f8a7e7e0a9f0beffbda05d08a7d', 16))
C = str(int('0x1694d7ad0d81ce96e2673abbdf3fbb8e18c6259f632a88002f3d662e9449878e2ba1d324c8d8008d8836832be433b097adfc87069568ea7cc9eb9f2a1e58d31cff07e79c95b4e38963ba182d42541aeb8617860301b3237ef08cc5ae86cd5c902fa06c5327b028969ceba1700124616f52a35f8a7e7e0a9f0beffbda05d08a7b', 16))

K = str(int('9b3ac1753e4210ad', 16))
M = str(int('55', 16))
N = str(int('55'))
print(len(A))
print(len(B))
print(len(C))
def smallConstantToLarge(number):
    if number == '0':
        return '0'
    string = ''
    number = int(number)
    while number > 0:
        string = str(number % 2) + string
        number = number // 2

    return string

def longCMP(num1, num2):
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1
    else:
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                return 1
            if num1[i] < num2[i]:
                return -1
        return 0


def AddZero(num1, num2):
    len1 = len(str(num1))
    len2 = len(str(num2))
    if len1 > len2:
        count = len1 - len2  
        num2 = '0' * count + num2  
    if len1 < len2:
        count = len2 - len1  
        num1 = '0' * count + num1  
    num1 = num1[::-1]  
    num2 = num2[::-1]
    return num1, num2


def LongAdd(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    result = ''
    carry = 0
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    num1 = num1[::-1]  
    num2 = num2[::-1]
    for i in range(len(num1)):  
        dischargeFirst = int(num1[i])
        dischargeSecond = int(num2[i])
        temp = dischargeFirst + dischargeSecond + carry
        result = str(temp % 2) + result
        carry = temp // 2
    return str(carry) + result

"""def LongAdd(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    result = ''
    carry = 0
   
    for i in range(len(num1)):  
        dischargeFirst = int(num1[i])
        dischargeSecond = int(num2[i])
        temp = dischargeFirst + dischargeSecond + carry
        result = str(temp % 2) + result
        carry = temp // 2
    # print("A + B = " + hex(int((str(carry) + Result), 2)) + '\n')
    return str(carry) + result"""


def longSub(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    result = ''
    borrow = 0
    cmp = longCMP(num1, num2)
    #print(cmp)
    if cmp == -1 or cmp == 0:
        for i in range(len(num1)):  
            dischargeFirst = int(num1[i])
            dischargeSecond = int(num2[i])
            temp = dischargeFirst - dischargeSecond - borrow
            if temp >= 0:
                result = str(temp) + result
                borrow = 0
            elif temp < 0:
                result = str(2 + temp) + result
                borrow = 1
        while result[0] != '1' and len(result) > 1:  
            result = result[1:]
        return result
    else:
        print('Віднімання від меншого більшого')

def longSub1(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    #print("A", str(num1))
    #print("\nB", str(num2))
    result = ''
    borrow = 0
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    num1 = num1[::-1]  
    num2 = num2[::-1]
    #print("A", num1)
    #print("\nB", num2)
    #cmp = longCMP(num1, num2)
    #print(cmp)
    for i in range(len(num1)):  
            dischargeFirst = int(num1[i])
            dischargeSecond = int(num2[i])
            temp = dischargeFirst - dischargeSecond - borrow
            if temp >= 0:
                result = str(temp) + result
                borrow = 0
            elif temp < 0:
                result = str(2 + temp) + result
                borrow = 1

    while result[0] != '1' and len(result) > 1:  
        result = result[1:]
 
    return result



def longMulOneDigit(num1, digit):
    num1 = str(num1)
    result = ''
    carry = 0
    digit = int(digit)
    
    for i in range(len(num1)):
        dischargeFirst = int(num1[i])
        temp = dischargeFirst * digit + carry
        result = str(temp % 2) + result
        carry = temp // 2
    
    while carry > 0:
        result = str(carry % 2) + result
        carry = carry // 2

    return result


def LongMul(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    num1 = num1[::-1]  
    num2 = num2[::-1]
    result = ''
    for i in range(len(num1)):
        temp = longMulOneDigit(num1, num2[i])
        temp = temp + '0' * i  
        result = LongAdd(result, temp)

    while result[0] != '1' and len(result) > 1:
        result = result[1:]

    return result



def longDiv(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    k = len(num2)
    R = num1
    Q = ''

    while longCMP(R, num2) == 1 or longCMP(R, num2) == 0:
        t = len(R)
        C = num2 + '0' * (t - k)  

        if longCMP(R, C) == -1:
            t -= 1
            C = num2 + '0' * (t - k)  

        R = longSub1(R, C)
        R = str(R)
        Q = LongAdd(Q, '1' + '0' * (t - k))
    return Q, R

"""def LongPowerWindow(A, B):
    t = 4  
    B = str(B)  
    m = len(B)
    C = '1'  

    D = ['1', A]  # Таблиця степенів A

    # Передобчислення таблиці степенів
    for i in range(2, (2**t)):
        D.append(LongMul(D[i - 1], A))

    for i in range(m - 1, -1, -1):
        C = LongMul(C, D[int(B[i], t)])  

        if i != 0:  
            for k in range(t):
                C = LongMul(C, C)  

    return C
"""
def LongPowerWindow(num1, num2):
    num2 = str(num2)  
    m = len(num2)
    C = '1'  
    current_power = num1  

    for i in range(m - 1, -1, -1):
        if num2[i] == '1':
            C = LongMul(C, current_power)  

        if i != 0:  
            current_power = LongMul(current_power, current_power)  

    return C


AA = 123564178
Al = smallConstantToLarge(A)
print(len(Al))
Bl = smallConstantToLarge(B)
print(len(Bl))
Cl = smallConstantToLarge(C)
AAl = smallConstantToLarge(AA)
Kl = smallConstantToLarge(K)
Ml = smallConstantToLarge(M)
N = smallConstantToLarge(N)
print("\nSmaltoLarge", Al)
A0, B0 = AddZero(Al,Bl)
#K0, M0 = AddZero(Kl, Ml)
#K0 = K0[::-1]
#M0 = M0[::-1]

result2 = longCMP(A0, B0)
if result2 == -1:
    print("\nA > B")
elif result2 == 0:
    print("\nA = B")
else:
    print("\nA < B")
A0, B0 = AddZero(Al,Bl)
print("\nAddZeroA", Al,"\nBl", Bl, "\nA0", A0,"\nB0", B0 )
D = LongAdd(Al,Bl)
print("\nA+B=", hex(int(D, 2)))
E = longSub(A0, B0)
print("\nA-B=", hex(int(E, 2)))
F = LongMul(Al, Bl)
print("\nA*B=", hex(int(F, 2)))
G = longMulOneDigit(A0, 3)
print("\nA*b=",hex(int(G, 2)))
H = longDiv(Al, Bl) [0]
J = longDiv(Al, Bl) [1]
print("\nЦіла частина=", hex(int(H, 2)), "\nОстача=", hex(int(J, 2)))
T = LongPowerWindow(Kl, Ml)
print("\nПіднесення до степеню=", hex(int(T, 2)))




print('Б1:')
res1 = LongMul(LongAdd(Al, Bl), Cl)
print('\n(a + b)*c = ', hex(int(res1, 2)))
res2 = LongMul(Cl, LongAdd(Al, Bl))
print('\nc*(a + b) = ', hex(int(res2, 2)))
res3 = LongAdd(LongMul(Al, Cl), LongMul(Bl, Cl))
print('\na*c + b*c = ', hex(int(res3, 2)))

if int(res1, 16) == int(res2, 16) and int(res2, 16) == int(res3, 16):
    print('\nВиконується')
else:
    print('\nНе виконується')

print('Б2:')
res4 = LongMul(N, Al)
print('\nn*a = ', hex(int(res4, 2)))
print(len(res4))
res5 = ''
for i in range(55):
    res5 = LongAdd(res5, Al)
    res5 = str(res5)

while res5[0] != '1' and len(res5) > 1:  
    res5 = res5[1:]
print(len(res5))
print('\na+...+a (n-разів)= ', hex(int(res5, 2)))
if res4 == res5:
    print('\nВиконуєьтся')
else:
    print('\nНе виконуєьтся')


print('\nВ:\n')
print('\nAdd')
cProfile.run('LongAdd(Al, Bl)')
print('\nSub')
cProfile.run('longSub(A0, B0)')
print('\nMul')
cProfile.run('LongMul(Al, Bl)')
print('\nDiv')
cProfile.run('longDiv(Al,Bl)')
print('\nLongPower')
cProfile.run('LongPowerWindow(Kl, Ml)')