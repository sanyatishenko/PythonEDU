###########################
# Работа с исключениями
###########################

# try:
# except "TypeOfExcept1":
# except "TypeOfExcept2":
# else:
# finally:

# https://docs.python.org/3.7/tutorial/errors.html

x =  input("Input number: ")
try:
    i = int(x)
    result = 100/i
except ValueError:
    print("This is not number!")
except ZeroDivisionError:
    print("This is Zero!")
else:
    print(result)
finally:
    print("The End!")
    