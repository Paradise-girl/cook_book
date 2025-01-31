
cook_book = {}
with open('cook.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
index = 0
while index < len(lines):
    dish_name = lines[index].strip()
    index += 1
    num_ingredients = int(lines[index].strip())
    index += 1
    ingredients = []
    for _ in range(num_ingredients):
        ingredient_line = lines[index].strip()
        index += 1
        ingredient_name, quantity, measure = ingredient_line.split(' | ')
        ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': int(quantity),
            'measure': measure})
    cook_book[dish_name] = ingredients

    if index < len(lines) and lines[index].strip() == '':
        index += 1

print(cook_book)

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(3, ['Запеченный картофель', 'Омлет'])


file_info = []
with open('1.txt', 'r', encoding='utf-8') as file:
    line_1 = {}
    count_1 = 0
    for line in file.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1

with open('2.txt', 'r', encoding='utf-8') as file:
    line_2 = {}
    count_2 = 0
    for line in file.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2

with open('3.txt', 'r', encoding='utf-8') as file:
    line_3 = {}
    count_3 = 0
    for line in file.readlines():
        count_3 += 1
        line_3['3.txt'] = count_3

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda item: item[1])
file_info.append(join)
#print(join)
#print(type(join))
names = []
for j in join:
    names.extend(j)
#print(names)
#print(type(names))

#print(' '.join(str(el) for el in names))
with open('result.txt', 'w', encoding='utf-8') as file_result:
    file_result.write('\n'.join(str(el) for el in names))















