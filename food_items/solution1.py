def describe_items(food_items, color):
    result = []
    for vals in food_items.values():
        temp_str = ''
        for val in vals.values():
            
            for key, v in val.items():
                if v['color'] == color:
                    temp_str = f'The {key} is {v["taste"]}.'
                    result.append(temp_str)
    return result

food_items = {
    'fruits': {
        'tropical': {
            'mango': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'vitamin A', 'fiber']
            },
            'pineapple': {
                'color': 'yellow',
                'taste': 'tangy',
                'nutrients': ['vitamin C', 'manganese', 'fiber']
            }
        },
        'temperate': {
            'apple': {
                'color': 'red',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'fiber', 'potassium']
            },
            'pear': {
                'color': 'green',
                'taste': 'juicy',
                'nutrients': ['vitamin C', 'fiber', 'copper']
            }
        }
    },
    'vegetables': {
        'leafy': {
            'spinach': {
                'color': 'green',
                'taste': 'earthy',
                'nutrients': ['vitamin K', 'vitamin A', 'iron']
            },
            'kale': {
                'color': 'green',
                'taste': 'bitter',
                'nutrients': ['vitamin K', 'vitamin A', 'calcium']
            }
        },
        'root': {
            'carrot': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin A', 'vitamin K', 'fiber']
            },
            'beet': {
                'color': 'red',
                'taste': 'earthy',
                'nutrients': ['vitamin C', 'folate', 'iron']
            }
        }
    }
}
result = describe_items(food_items, 'red')
print(result)