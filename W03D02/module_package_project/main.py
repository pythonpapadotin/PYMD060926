import fruits as fruits_independent_module

from food import vegetables, fruits

import food

patient_nutrient = input('Which Nutrient you want?')

result = fruits.find_fruit_by_nutrient(patient_nutrient)

print(f"Start Eating {','.join(result)}")

veg_name = 'ladyfinger'
result2 = vegetables.is_vegetable_present(veg_name)

print(veg_name, result2)
