def sum(arr):

    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum(arr[1:])


