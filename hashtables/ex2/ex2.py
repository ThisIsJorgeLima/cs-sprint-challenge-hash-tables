
#  Hint:  You may not need all of these.  Remove the unused functions.


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    # Now lets go through each ticket that are stored
    for i in tickets:
        cache[i.source] = i.destination

    route = []

    # k will traverse the keys
    # v will taverse the values
    # our for-loop:
    for k, v in cache.items():
        if k == "NONE":
            route.append(v)

    complete_ticket = False
    # while loop:
    while not complete_ticket:
        previous_stop = route[-1]

        if previous_stop in cache.keys():
            route.append(cache[previous_stop])

        if previous_stop == "NONE":
            complete_ticket = True

    return route[:length]
