##############################
# Объявляем переменные
##############################
i = 3
t = 'text'
a,b,c = 1, 2+2, "test"

##############################
# Область видимости переменных
##############################

#Локальные переменные
a = 1
def f():
  a = 2
  print(a)

f()
print(a)
# Результат 2 1 т.к. в функции f() создается локальная переменная

#Глобальные переменные
a = 1

def ff():
  global a  #Указываем на использование глобальной переменной
  a = 2     #Изменяем глобальную переменную
  print(a)

ff()
print(a)
# Результат 2 2 т.к. в функции f() изменяется глобальная переменная

#Использование переменной родительского контекста
a = 1
def f1():
  a = 2         # Создает локальную переменную
  def f2():
    nonlocal a  # Берёт переменную 'a' из функции f1() 
    a = 3
    print(a)    # выводит 3
  f2()
  print(a)      # выводит 3

f1()
print(a) # выводит 1

#############################
# Константы
#############################

# Python не имеет неизменяймых переменных
# принято переменные, которые не предпологается изменять, объявлять в верхнем регистре
PI = 3.14

#############################
# Операторы присваивания
#############################
a = 1
b = 2
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a %= b  # a = a % b