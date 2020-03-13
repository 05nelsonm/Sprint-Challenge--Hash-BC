#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    destination = "NONE"
    counter = 0
    while counter < length:
        current_ticket = hash_table_retrieve(hashtable, destination)
        destination = current_ticket
        route[counter] = destination
        counter += 1

    return route[:-1]
