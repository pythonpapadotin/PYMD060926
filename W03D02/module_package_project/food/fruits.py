# This is considered as a module in python
# This is a fruit module in food package

basic_info = {
    "number_of_fruits": 5,
    "data": [
        {"name": "apple",
         "tagline": "An apple a day, keeps doctor away!",
         "nutrients": ['Vitamin A', 'Fiber']},
        {"name": "mango",
         "tagline": "In India, People eat me a lot!",
         "nutrients": ['Vitamin C', 'Fiber']},
        {"name": "kiwi",
         "tagline": "I am sour in taste!",
         "nutrients": ['Vitamin C', 'Protein']},
        {"name": "Guava",
         "tagline": "I come in various colors like green, pink, etc",
         "nutrients": ['Vitamin A', 'Protein']},
        {"name": "Avocado",
         "tagline": "People love to create sandwhich and shake with me!",
         "nutrients": ['Vitamin K', 'Fiber']},
    ]
}


def find_fruit_by_nutrient(search_nutrient):
    fruit_data = basic_info.get("data")
    final_fruit_list = []
    for fruit in fruit_data:
        nutrient_in_fruit = fruit.get('nutrients')
        for nutrient_present in nutrient_in_fruit:
            if search_nutrient == nutrient_present:
                final_fruit_list.append(fruit.get('name'))
    return final_fruit_list
