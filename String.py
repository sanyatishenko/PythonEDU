############################
# Работа со строками
############################

s = "This string"                   # This string
S = 'And this string'               # And this string
Q = 'String with "string"'          # String with "string"
q = "String with other 'string'"    # String with other 'string'
w = 'I\'m not a quote'              # I'm not a quote
W = 'I am \n a new line'            # I am -> a new line
t = 'I am \t a Tab'                 # I am     a Tab
print("C:\Folder\new")              # C:\Folder -> ew
print(r"C:\Folder\new")             # C:\Folder\new
b = ''' This is
        big string'''
print(b)                            # This is \n\t\t big string
fname = 'jon'
lname = "sNoW"
print(fname * 2)                    # jonjon
name = fname + " " + lname          # jon sNoW
print(name.title())                 # Jon Snow
print(name.upper())                 # JON SNOW
print(name.lower())                 # jon snow
Str = "   ---Test---   "
print(Str.lstrip())                 # ---Test---   # end of string
print(Str.rstrip())                 #    ---Test---# end of string
print(Str.strip())                  # ---Test---# end of string
print(Str.strip().strip("-"))       # Test
print(len(name))                    # 8
print(name[0])                      # j # 0 - первый символ 1 - второй
print(name[-1])                     # w # -1 - последний символ -2 предпоследний
print(name[1:5])                    # on s
print(name[2:])                     # n sNoW
print(name[:2])                     # jo
print(name[2::2])                   # nso # jo(n) (s)N(o)W 
print(name[:6:2])                   # jns # (j)o(n) (s)NoW
print(name[::-1])                   # WoNs noj
print(name.find('N'))               # 5
print(name.replace('o','0'))        # j0n sN0W
print(name.split('o'))              # ['j', 'n sN', 'W']
print("O".join(['j', 'n sN', 'W'])) # jOn sNOW
print(name.count('o'))              # 2

###########################
# Форматирование строк
###########################
string = 'This is {0} test string{1}'
print(string.format('first','!'))               # This is first test string!
string = 'This is {number} test string{end}'
print(string.format(number='second',end='!!!')) # This is second test string!!!