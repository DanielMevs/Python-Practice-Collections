def insert_item(my_tuple, new_value, index):
    # Your code goes here

    return my_tuple[:index] + (new_value, ) + my_tuple[index: ]