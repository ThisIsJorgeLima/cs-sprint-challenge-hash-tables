def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length == 1:
        return None
        # if condition ; else if
    elif length == 2:
        first_number = weights[0]
        second_number = weights[1]
        if first_number + second_number == limit:
            return [1, 0]
        else:
            return None

    else:
        cache = {}
        answer = []

        # now using a for-loop to iterate and compute 0, length
        for i in range(0, length):
            cache[weights[i]] = i

            # k will traverse the keys
            # v will taverse the values
            # our for-loop:
        for k, v in cache.items():
            if limit - k in cache.keys():
                # add on and updates
                answer.append(v)
                # if True, the sorted list is reversed in descending order
        return sorted(answer, reverse=True)
