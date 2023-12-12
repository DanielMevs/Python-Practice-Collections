def prepare_list(animals):
    result = set()
    for animal in animals:
        result.add(animal)
    return sorted(result)