#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove,
                        # hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)
    for lp in ht.storage:
        if lp:
            next_key = limit - lp.key
            if next_key in weights:
                next_index = hash_table_retrieve(ht, next_key)
                if next_index != lp.value:
                    if lp.key <= next_key:
                        return (next_index, lp.value)
                    else:
                        return (lp.value, next_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
