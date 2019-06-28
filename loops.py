#################################
# Циклы
#################################

# Цикл While
a = 0
while a < 5:
    print(a)
    a += 1
# Результат 0 1 2 3 4

# Цикл For
for i in 0,1,'test',3.5 :
    print(i)
# Результат 0 1 test 3.5

# оператор continue переход к следующей итерации
for i in range(4) :
    if i == 1 :
         continue
    else :
         print(i)
# Результат 0 2 3

# оператор break завершает цикл
for i in 0,1,'test',3.5 :
    if i == 'test' : break
    print(i)
# Результат 0 1

# else выполняется если не выполнился break
for i in range(1,7,2) :
    if i == 4 : break
    print(i)
else :
    print("Число 4 не найдено в массиве")
# Результат 1 3 5 'Число 4 не найдено в массиве'