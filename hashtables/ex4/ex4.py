def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    numbers_with_negatives = []

    for number in a:

        # lets add all of our numbers to our dictionary
        cache[number] = 1

        # if our current number are inversly added into our dictionary, will add the positive to the outcome of our array
        # and will exclude zero

        # if number is not equal to:
        if number != 0 and -number in cache:
            # will add on [append] and return our absolute value
            numbers_with_negatives.append(abs(number))

    return numbers_with_negatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
