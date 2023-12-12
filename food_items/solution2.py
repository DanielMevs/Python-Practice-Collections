def describe_items(food_items, color):
    result = []
    for food in food_items:
        for type in food_items[food]:
            for item in food_items[food][type]:
                if food_items[food][type][item]['color'] == color:
                    result.append(f"The {item} is {food_items[food][type][item]['taste']}.")
    return result