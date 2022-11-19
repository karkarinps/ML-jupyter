""" n = input()
m = n.count('f')
if m==0:
    print('NO')
elif m==1:
    print(n.find('f'))
elif m>1:
    print(n.find('f'), n.rfind('f'), sep=' ') """

""" l = [input() for i in range(int(input()))] 
w = input()
[print(i) for i in l if w.lower() in i.lower()] """

""" l = [i for i in input().split(' ') if i.lower() in ['a', 'an', 'the']]
print(f'Общее количество артиклей: {len(l)}') """

""" l = [int(input()) for i in range(int(input()))] 
[print(i) for i in l if i<0]
[print(i) for i in l if i==0]
[print(i) for i in l if i>0] """

""" l = list(map(int, input().split(' ')))
minel = l.index(min(l))
maxel = l.index(max(l))
l[minel], l[maxel] = l[maxel], l[minel]
print(*l) """

""" l = input().split()
[print('+'*int(i)) for i in l] """


""" print('ДА') if all(map(lambda x: 0<=int(x)<=255, input().split('.'))) else print('НЕТ') """

""" n = int(input())
print([i for i in range(1, n+1) if n%i==0]) """

""" l = [int(input()) for i in range(int(input()))]
[print(i) for i in l if i!=min(l) and i!=max(l)] """

""" l = []
[l.append(input()) for i in range(int(input()))]
print(list(''.join(l))) """

""" print([int(input()) for i in range(int(input()))][::2]) """


""" num_a = int(input())
num_b = int(input())
for i in range(num_a, num_b+1):
    flag = 1
    for j in range(2, i+1):
        if i!=j and i%j == 0:
            flag = 0
    if flag == 1 and i!=1:
        print(i) """

""" bin(int(input())) """

""" w = input()
print(w[2], w[-2], w[:5], w[:-2], w[::2], w[1::2], w[::-1], w[-1::-2], sep = '\n') """

""" w = list(input())
print(''.join(list(map(lambda x: x.upper() if x.islower() else x.lower(), w)))) """

""" w = input()
print('YES') if w.endswith('.com') or w.endswith('.ru') else print('NO') """


""" n = int(input())
count = 0
for i in range(n):
    word = input()
    if word.count('11')>2:
        count+=1
print(count) """


""" a = input()
glas = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
count_gl = 0
count_so = 0
for i in a:
    if i in glas:
        count_gl += 1
    elif i in sogl:
        count_so += 1
print(f'Количество гласных букв равно {count_gl}')
print(f'Количество согласных букв равно {count_so}') """



""" n = int(input())
fact_sum = 1
for j in range(2, n+1): 
    factorial = 1
    for i in range(2, j+1):
        factorial *= i
    fact_sum += factorial
print(fact_sum) """

""" while len(num_1)>1:
    num_1 = list(str(sum(list(map(lambda x: int(x), num_1)))))
print(*num_1) """

""" num_2 = int(input())
sum_div = 0
num_div = 0
for i in range(num_1, num_2+1):
    sum_div_syc = 0
    for j in range(1, i+1):
        if i%j == 0:
            sum_div_syc += j
    if sum_div <= sum_div_syc:
        sum_div = sum_div_syc
        num_div = i
print(num_div, sum_div, sep = ' ') """