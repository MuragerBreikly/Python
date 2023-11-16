#LEVEL1 
#1 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
print(len(it_companies)) 
#2 
it_companies.add('Twitter') 
print(it_companies) 
#3 
it_companies.update({'Python','CSS','Html'}) 
print(it_companies) 
#4 
it_companies.remove('Google') 
print(it_companies) 
#5 
 
#LEVEL2 
A = {"d", "z", "a"} 
B = {3, 4, 5} 
 
#1 
inter = A.intersection(B) 
print(" B", inter) 
 
# 2 
isasubset = A.issubset(B) 
print("A and B", isasubset) 
 
#3 
isdisjoint = A.isdisjoint(B) 
print("A B ", isdisjoint) 
 
# 4 
unionAB = A.union(B) 
unionBA = B.union(A) 
print("A and B union", unionAB) 
print("union B and A:", unionBA) 
 
#5 
symmetric_difference = A.symmetric_difference(B) 
print("symetric A and B", symmetric_difference) 
 
#6 
del A 
del B 
# LEVEL3 
# 1 
age = [25, 30, 35, 40] 
agesset = set(age) 
 
# 1a 
if len(age) > len(agesset): 
    print("сптсоктын длинасы набордан улкен") 
else: 
    print("набордын длинасы списоктан улкен") 
 
# 2 
konspekt = """ 
string - дегеніміз таңбалары өзгермейтін тізбек, текст 
list - әртүрлі бола алады, және өзгереді 
tuple - жазған элементтер өзгертілмейді! Тьюплға ештеңе қосылмайды және алынбайды. Бір элемент қосу үшін жаңа Тьюплға қосамыз 
set - дубликаттар болмайтын колекция, дубликаттарды сеттің ішіне сақтай алмаймыз екі рет қайталанбайды set те индекс жок, ретсіз орналасқан, 
""" 
print("айырмашылықтары \n", konspekt) 
# 3 
sentenc = " I am a teacher and I like to inspire and teach people. " 
don = set(sentenc.split()) 
lili = len(don) 
print("уникальные слово", lili)