#################################
# Работа со списками - массивы
#################################

array = [1,5,3,7,8,9,3,4]
Cheeses = ['Gauda','Mozzarella','Parmesan','Feta','Brie','Camembert','Cheddar','Gorgonzola']

print(Cheeses[0])               # Gauda
print(Cheeses[-1])              # Gorgonzola

array[3] = 2
print(array)                    # [1, 5, 3, 2, 8, 9, 3, 4]

array.append(10)
print(array)                    # [1, 5, 3, 2, 8, 9, 3, 4, 10]

array.insert(2,6)
print(array)                    # [1, 5, 6, 3, 2, 8, 9, 3, 4, 10]

array.sort()
print(array)                    # [1, 2, 3, 3, 4, 5, 6, 8, 9, 10]

array.remove(3)
print(array)                    # [1, 2, 3, 4, 5, 6, 8, 9, 10]

array.pop(4)                     
print(array)                    # [1, 2, 3, 4, 6, 8, 9, 10]

array[:2] = []
print(array)                    # [3, 4, 5, 6, 8, 9]

NewArray = array                # Списки связываются !!!
print('NewArray:',NewArray)     # NewArray: [3, 4, 6, 8, 9, 10]
array.pop()
print('NewArray:',NewArray)     # NewArray: [3, 4, 6, 8, 9]

NewArray2 = array.copy()        # Создается независимая копия списка
print('NewArray2:',NewArray2)   # NewArray: [3, 4, 6, 8, 9, 10]
array.pop()
print('NewArray2:',NewArray2)   # NewArray: [3, 4, 6, 8, 9]

#############
# Срезы
#############

# list[begin:end:step]
print(Cheeses[::2])             # ['Gauda', 'Parmesan', 'Brie', 'Cheddar']
print(Cheeses[::-1])            # ['Gorgonzola', 'Cheddar', 'Camembert', 'Brie', 'Feta', 'Parmesan', 'Mozzarella', 'Gauda']

Cheeses[:3] = ['Янтарь','Плавленный','Колбасный']
print(Cheeses)                  # ['Янтарь', 'Плавленный', 'Колбасный', 'Feta', 'Brie', 'Camembert', 'Cheddar', 'Gorgonzola']

del Cheeses[3:-2]
print(Cheeses)                  # ['Янтарь', 'Плавленный', 'Колбасный', 'Cheddar', 'Gorgonzola']