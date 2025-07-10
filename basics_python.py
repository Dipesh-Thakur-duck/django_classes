def even_check(num):
    return num % 2 == 0

if even_check(2):
    print("even")
else:
    print("odd")
even_check(2)

def even_upto_hundred():
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
        i += 1

names = ['Sujan', 'Rija', 'Sharmila', 'Dipesh', 'Nikita', 'Sima', 'Kusum']

def find(names,find):
    for i in names:
        if i == find:
            return True
print(find(names,'Sujan'))

names_1 = ['Sujan','Sujan', 'Harish']

print(list(set(names_1)))

def second_largest(list):
    list.sort()
    return list[len(list) - 2]

print(second_largest([1,2,3,4,5]))

names_roll = {'1':{
    'name':'Dipesh',
    'age':21,
    'salary':20000
},'2':{
    'name':'Nikita',
    'age':21,
    'salary':18000
}}

print(names_roll['1'])

for key,values in names_roll.items():
    for key,value_1 in values.items():
        print(value_1)
        