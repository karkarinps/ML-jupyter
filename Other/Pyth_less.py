"""Ransom Note"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_list = list(ransomNote)
        [ran_list.remove(i) for i in magazine if i in ran_list]
        res = ''
        if len(ran_list) == 0:
            res = True
        else:
            res = False
        return print(res)
        
p = Solution()
p.canConstruct(ransomNote = 'aa', magazine = 'aab')

-----------------------------------------------------------


"""Палиндром?"""

def isPalindrome(head):
    head_list = list(head)
    res = ''
    if len(head_list)%2 == 0:
        if head_list[:int(len(head_list)/2)] == head_list[int(len(head_list)/2):][::-1]:
            res = True
        else:
            res = False
    else:
        if head_list[:int(len(head_list)//2)] == head_list[int((len(head_list)//2)+1):][::-1]:
            res = True
        else:
            res = False
    return print(res)

head = '1234321'
isPalindrome(head)

------------------------------------------


"""roman to int"""
def romanToInt(s):
    dict_rom = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    rom_list = list(s)
    int_list = []
    for i in rom_list:
        int_list.append(dict_rom[i])
    int_list.append(0)
    int_sort = []
    for j in range(len(int_list)-1):
        if int_list[j] >= int_list[j+1]:
            int_sort.append(int_list[j])
        else:
            int_sort.append(-int_list[j])

    return print(sum(int_sort))

s = 'MCMXCIV'
romanToInt(s)


-----------------------------------------------------------------
from functools import reduce
with open('logfile.txt', 'r', encoding='utf-8') as f_1, open('output.txt', 'w', encoding='utf-8') as out_1:
    a=[i.strip().split(', ') for i in f_1.readlines()]
    b=[[j.split(':') for j in i if ':' in j] for i in a]
    c=[[reduce(lambda x, y: int(x)*60+int(y), j) for j in i] for i in b]
    d=[reduce(lambda x, y: x-y, i) for i in c]
    print(*{a[i][0]: d[i] for i in range(len(a)) if abs(d[i])>=60}, sep='\n', file=out_1)

-----------------------------------------------------------

""" abcdefghijklmnopqrstuvwxyz
абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя """

""" Алгоритм дешифровки шифра Цезаря с постояным сдвигом на рандомное значение. 
Зададим функцию, которая будет сдвигать буквы на заданную величину """
def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index - num < 0:
        if symb.lower() == symb:
            return abc[symb_index - num + len(abc)]
        else:
            return abc[symb_index - num + len(abc)].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index - num]
        else:
            return abc[symb_index - num].upper()


""" Фраза для дешифровки """
wor = input().split()                
print(wor)
"""  Диапазон предполагаемого сдвига, можно задавать любой """
range_shift = range(0, 26)     
for i in range_shift:
    ces_list = []
    for j in wor:
        ces = ''
        for k in j:
            if k.isalpha():
                ces += sdvig(k, i)
            else:
                ces += k
        ces_list.append(ces)
    print(' '.join(ces_list))
    print(i)


""" Конец дешифратора Цезаря """



          
""" Шифр Цезаря - сдвинуть каждый символ вводимой строки на длину слова в котором он находится """

""" задаём функцию сдвига каждого символа symb на num позиций в алфавите в том же регистре """
""" def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper() """
""" разделение фразы на слова, побуквенное просеивание каждого слова, чтобы получить длину слова без лишних знаков
Затем побуквенная подстановка буквы в функцию со сдвигом равным длине слова - списка
Добавление сдвинутых букв в промежуточную пустую строку, затем добавление этой строки в пустой лист для получения
сдвинутой фразы.
Объединение списка по пробелам через джоин. """
""" ces_list = []
wor = input().split()
print(wor)
for i in wor:
    wor_list = []
    ces = ''
    for j in i:
        if j.isalpha():
            wor_list.append(j)
    for k in i:
        num = len(wor_list)
        if k.isalpha():
            ces += sdvig(k, num)
        else:
            ces += k
    ces_list.append(ces)
print(' '.join(ces_list)) 

Конец кода шифра Цезаря"""


""" 
def compute_binom(n, k):
    n_fac = 1
    for i in range(1, n+1):
        n_fac *= i
    k_fac = 1
    for i in range(1, k+1):
        k_fac *= i 
    n_k_fac = 1
    for i in range(1, n-k+1):
        n_k_fac *= i
    return int(n_fac/(k_fac*n_k_fac))


n = int(input())
k = int(input())


print(compute_binom(n, k)) """


""" 
def is_magic(date):
    if int(date[:2])*int(date[3:5])==int(date[-2:]):
        return True
    else:
        return False


date = input()


print(is_magic(date)) """


""" d = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 0: ' '}


def number_to_words(num):
    if num<=20:
        return d[num]
    else:
        return d[num-num%10]+' '+d[num%10]


n = int(input())


print(number_to_words(n)) """

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

""" s = input()
news = ''
for i in range(len(s)):
    if i%3!=0:
        news += s[i]
print(news) """

""" s = input()
news = s[:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+s[s.rfind('h'):]
print(news)   """    


""" print(list(range(2, int(input())+1))[::2]) """

""" list1 = [int(i) for i in input().split(' ')]
list2 = [int(i) for i in input().split(' ')]
output = []
for i in range(len(list1)):
    output.append(list1[i]+list2[i])
print(*output) """

""" s = input().split(' ')
list_num = [int(i) for i in s]
list_sum = [i+'+' for i in s]
list_sum[-1] = s[-1]+'=' 
print(''.join(list_sum), sum(list_num), sep='') """

""" s = input().split('-')

try:
    if len(s)==3 and len(s[-1])==4 and s[-1].isdigit()==True and len(s[-2])==3 and s[-2].isdigit()==True and len(s[-3])==3 and s[-3].isdigit()==True:
        flag = 1
    elif len(s)==4 and len(s[-1])==4 and s[-1].isdigit()==True and len(s[-2])==3 and s[-2].isdigit()==True and len(s[-3])==3 and s[-3].isdigit()==True and len(s[-4])==1 and int(s[-4])==7:
        flag = 1
    else:
        flag = 0
except:
    flag = 0

if flag == 1:
    print('YES')
else:
    print('NO') """


""" print(max([len(i) for i in input().split(' ')])) """


""" print(*[i[1:]+i[0]+'ки' for i in input().split(' ')]) """


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
