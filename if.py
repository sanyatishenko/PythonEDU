###################################
# Условный оператор if-elif-else
###################################

a = int(input('Введите число: '))
if a < 0 :
    print("Число", a,"отрицательное.")
elif a == 0 :
    print("Ноль.")
else : 
    print("Число", a,"положительное.")

# Короткая запись if
print(a,"не равно нулю") if a else print("Ноль")