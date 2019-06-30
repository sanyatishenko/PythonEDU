#############################
# Работа с модулями
#############################

# импортируем стандартный модуль random

import random
 
x = random.randint(1,100)               # Обращение к функции модлуя идиет через имя модуля
print("Random number: " + str(x))       # Random number: 79

# импортируем все функции модуля

from mymodule import *
x = 5
f = factor(x)                           # Обращение к функции модлуя идиет без имени модуля
print("Factor ",x,"!\t=\t",f)           # Factor  5 !     =        120

# Псевдонимы модулей

import math as m                        # Обращение к функции модлуя идиет через псевдоним

print("Pi = ",m.pi)

from time import time_ns as ns          # Импорт из модуля одной функции и обращение к ней по псевдониму

print("Time in nanoseconds since Epoche: ",ns())    # Time in nanoseconds since Epoche:  1561900996775119600