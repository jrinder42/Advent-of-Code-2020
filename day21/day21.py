
'''

Advent of Code 2020 - Day 21

'''

allergens = {}
allergens_raw = []
with open('day21.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if ')' in line:
            ingredients = line[:line.index('(') - 1].split(' ')
            ingredients = [ingredient.strip() for ingredient in ingredients]
            allergens_raw += ingredients

            allergen_list = line[line.index('(') + 1:line.index(')')].split(',')
            allergen_list[0] = allergen_list[0].split('contains ')[1]
            allergen_list = [al.strip() for al in allergen_list]
            for allergen in allergen_list:
                if allergen in allergens:
                    allergens[allergen] = set(allergens[allergen]).intersection(ingredients)
                else:
                    allergens[allergen] = set(ingredients)

# Part 1

allergens_unique = {}
while len(allergens_unique) != len(allergens):
    for key, value in allergens.items():
        if key in allergens_unique:
            continue
        else:
            if len(value) == 1:
                allergens_unique[key] = value.pop()
            else:
                modified_allergens = set()
                for allergen in value:
                    if allergen in allergens_unique.values():
                        modified_allergens.add(allergen)

                allergens[key] = set(allergens[key]).symmetric_difference(modified_allergens)

not_possible_ingredients = []
for ingredient in allergens_raw:
    if ingredient not in allergens_unique.values():
        not_possible_ingredients.append(ingredient)

print('Advent of Code Day 21 Answer Part 1:', len(not_possible_ingredients))

# Part 2

sorted_allergens = sorted(allergens_unique.keys(), key=lambda x: x)

dangerous_ingredient_list = ''
for key in sorted_allergens:
    dangerous_ingredient_list += allergens_unique[key] + ','
dangerous_ingredient_list = dangerous_ingredient_list[:-1]

print('Advent of Code Day 21 Answer Part 2:', dangerous_ingredient_list)






