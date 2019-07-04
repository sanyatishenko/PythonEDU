###############################
# Работа с файлами
###############################

read_file_path = "files/IPs.txt"
write_file_path = "files/out.txt"

f = open(read_file_path, "r", encoding="utf8")
w = open(write_file_path, "w", encoding="utf8")

# num помещаем номер стоки, номерацию начинаем с 1
# line помещаем содержание строки
for num, line in enumerate(f,1):                
    text = "Line# "+str(num)+": "+line.strip()
    print(text)
    w.write(text+'\n')

f.close()
w.close()

