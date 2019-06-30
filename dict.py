#################################
# Словари (структуры)
#################################

#       |--------Item--------|
#       |--Key--||---Value---|

tea = {
        'Name':   'Tieguanyin',
        'Color':  'oolong',
        'Price':  10
}

coffee = dict(kind='arabica',country='Brasil',price=20)

print(tea)                  # {'Name': 'Tieguanyin', 'Color': 'oolong', 'Price': 10}
print(coffee)               # {'kind': 'arabica', 'country': 'Brasil', 'price': 20}
print(tea.keys())           # dict_keys(['Name', 'Color', 'Price'])
print(tea.values())         # dict_values(['Tieguanyin', 'oolong', 10])
print(tea['Name'])          # Tieguanyin

tea['country'] = 'China'
print(tea)                  # {'Name': 'Tieguanyin', 'Color': 'oolong', 'Price': 10, 'country': 'China'}

tea['Price'] += 5
del tea['Color']
print(tea)                  # {'Name': 'Tieguanyin', 'Price': 15, 'country': 'China'}

for v, k in tea.items():
        print(str(v)+": "+str(k))       # Name: Tieguanyin \n Price: 15 \n country: China