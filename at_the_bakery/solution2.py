def build_menu(cakes):
    # Your code goes here
    cakes[105] = ['Coffee', 1.49]
    result = []
    for val in cakes.values():
        temp_str = f'{val[0]} Cake - ${val[1]}'
        result.append(temp_str)

    return list(reversed(sorted(result)))