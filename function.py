#######################
# Работа с функциями
#######################

# Передача параметров, позиционные параметры
def summa(x, y):
    return x+y

print(summa(12,13))                         # 25

# Любое число параметров
def summa2(*array):
    result = 0
    for i in array:
        result += i
    return result

print(summa2(1,4,6,9,15,2,0))               # 37

# Именованые параметры, параметры по умолчанию
def Hello(fname,lname,sname=''):
    print('Hello ' + fname.title()+" "+sname.title()+" "+lname.title())

Hello(lname = "Харламов", fname = "Гарик")  # Hello Гарик  Харламов
Hello("Гарик","Харламов","Бульдог")         # Hello Гарик Бульдог Харламов

name = ["Тимур","Батрудинов","Каштан"]
Hello(*name)                                # Hello Тимур Каштан Батрудинов