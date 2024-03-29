"""Longest Palindromic Substring"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1 or s==s[::-1]:
            return s
        longest = ''
        for i in range(len(s)):
            if (s[:-i]==s[:-i][::-1] and s[:-i] and len(longest)<len(s[:-i])):
                longest = s[:-i]
            if s[i:]==s[i:][::-1] and s[i:] and len(longest)<len(s[i:]):
                longest = s[i:]            
            for j in range(len(s[:-i])):               
                if s[:-i][j:]==s[:-i][j:][::-1] and s[:-i][j:] and len(longest)<len(s[:-i][j:]):
                    longest = s[:-i][j:]
                if s[i:][:-j]==s[i:][:-j][::-1] and s[i:][:-j] and len(longest)<len(s[i:][:-j]):
                    longest = s[i:][:-j]

        return longest

---------------------------------------

"""Can Make Arithmetic Progression From Sequence - On"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        k=arr[1]-arr[0]
        for i in range(len(arr)):
            if arr[i]!=arr[-1] and arr[i+1]-arr[i]!=k:
                return False
        return True

------------------------------------------------------------
"""Can Make Arithmetic Progression From Sequence - On"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        k = min(arr)
        arr_1 = arr
        arr_1.remove(k)
        n = min(arr_1)-k
        print(n, k)
        for i in range(len(arr)):
            k = min(arr_1)
            arr_1.remove(k)
            if arr_1 and min(arr_1)-k != n:
                return False
        return True 

-------------------------------------------------------------
"""Best Time to Buy and Sell Stock - On*2 complexity"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = 0
        for i in range(len(prices)):
            k = max(prices[i:]) - prices[i:][0]
            if k>d:
                d=k
        return d

"""Best Time to Buy and Sell Stock - BRUTE FORCE On**2 complexity"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = [0]
        for i in prices:
            dd = []
            for j in prices[prices.index(i)+1:]:
                if i-j<0:
                    dd.append(j-i)
            if dd:
                d.append(max(dd))
        return max(d)

---------------------------------------------------------

"""Remove Duplicates from Sorted List"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return ListNode('')
        l = set()
        while head:
            l.add(head.val)
            head = head.next
        res_list = list(l)
        res_list.sort()
        head = ListNode(res_list[0])
        tail = head
        e = 1
        while e < len(res_list):
            tail.next = ListNode(res_list[e])
            tail = tail.next
            e+=1
        return head

------------------------------------------------

"""Merge Two Sorted Lists"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = []
        list_l2 = []
        while list1:
            list_l1.append(str(list1.val))
            list1 = list1.next
        
        while list2:
            list_l2.append(str(list2.val))
            list2 = list2.next
        
        res_list=list_l1+list_l2
        res_list.sort(key=lambda x: int(x))
        if res_list:
            head = ListNode(res_list[0])
            tail = head
            e = 1
            while e < len(res_list):
                tail.next = ListNode(res_list[e])
                tail = tail.next
                e+=1
            return head
        else:
            return ListNode('')
        
----------------------------------------------------
"""Length of Last Word"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for i in s.rstrip()[::-1]:
            if i!=' ':
                cnt+=1
            else:
                break
        return cnt

----------------------------------------------------


"""Valid Parentheses"""
s = '{[]}'
par_dict = {'(':1, ')':-1, '{':1, '}':-1, '[':1, ']':-1}
l = [0, 0, 0, 0, 0, 0]
for i in s:
    l[list(par_dict).index(i)] += par_dict[i]
    if sum(l) < 0:
        break
if sum(l[:2])==sum(l[2:4])==sum(l[4:6]):
    print(True)
else:
    print(False)

---------------------------------------

"""Longest Common Prefix"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = max(strs, key=len)
        for i in range(len(strs)):
            if longest:
                long_2 = ''
                for j in range(len(strs[i])):
                    if j+1<=len(longest) and strs[i][j]==longest[j]:
                        long_2+=strs[i][j]
                    else:
                        break
                longest = long_2
            else:
                break     
        return longest
    
----------------------------------------------


"""Longest Substring Without Repeating Characters"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        res.sort(key=lambda x:len(x), reverse=True)
        
        for i in res:
            if len(set(i))==len(i) and len(i):
                return len(i)
                break
            
        return 0
    
------------------------------------------

"""Add Two Numbers"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = []
        list_l2 = []
        while l1:
            list_l1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            list_l2.append(str(l2.val))
            l2 = l2.next
        
        res_list = [int(i) for i in list(str(int(''.join(list_l1[::-1])) + int(''.join(list_l2[::-1]))))[::-1]]
        
        head = ListNode(res_list[0])
        tail = head
        e = 1
        while e < len(res_list):
            tail.next = ListNode(res_list[e])
            tail = tail.next
            e+=1

        return head

--------------------------------------------------


"""Two Sum"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in nums:
                if nums[i]+j==target and i!=nums.index(j):
                    return [i, nums.index(j)]

-------------------------------------------------------------------------

"""Richest Customer Wealth"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = 0
        for i in accounts:
            if sum(i)>n:
                n = sum(i)
        return n

--------------------------------------------------------------

"""Number of Steps to Reduce a Number to Zero"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = 0
        while num>0:
            if num%2==0:
                num = num//2
            elif num%2!=0:
                num-=1
            n += 1
        return n
    

---------------------------------------------------


"""The K Weakest Rows in a Matrix"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = [(mat[i].count(1),i) for i in range(len(mat))]
        res_1 = sorted(res)
        last_res = [res_1[i][1] for i in range(k)]
        return last_res

------------------------------------------------
""" Middle of the Linked List """

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listHead = []
        while head:
            listHead.append(head.val)
            head = head.next
        res_list = listHead[range((len(listHead)//2)+1)[-1]:]
        
        head = ListNode(res_list[0])
        tail = head
        e = 1
        while e < len(res_list):
            tail.next = ListNode(res_list[e])
            tail = tail.next
            e+=1

        return head
    
---------------------------------------------------------------

"""fizzBuzz"""

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        n_list = [i for i in range(1, n+1)]
        for i in n_list:
            if i%15==0:
                n_list[i-1] = 'FizzBuzz'
            elif i%5==0:
                n_list[i-1] = 'Buzz'
            elif i%3==0:
                n_list[i-1] = 'Fizz'
        n_list_2 = [str(i) for i in n_list]
        return print(n_list_2)

p = Solution()
p.fizzBuzz(15)

--------------------------------------

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

--------------------------------

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits)))+1)))
    
------------------------------------
