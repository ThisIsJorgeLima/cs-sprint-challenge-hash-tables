def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for array in arrays:
        # create a dictionary with counts for each int in our list of arrays:
        # for-loop
        for i in array:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

    result = []

    # return only the items that are equal to the length of our arrays

    for key, value in cache.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays.append(list(range(1, 5)) + [1, 2, 3])
    arrays.append(list(range(5, 11)) + [1, 2, 3])
    arrays.append(list(range(11, 16)) + [1, 2, 3])
    print(intersection(arrays))
