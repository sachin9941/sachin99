from collections import Counter
a = input('enter any string:')
b = ['a','e','i','o','u']
c = Counter(a)
print(c)
for x in b:
 
    print(f' vowels :{x} :',c[x])