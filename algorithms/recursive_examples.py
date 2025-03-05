def character_count(arr):
    if len(arr) == 0:
        return 0
    
    return len(arr[0]) + character_count(arr[1:])


# print(character_count(["ab", "c", "def", "ghij"]))


def even_numbers(arr):

    collection = []

    if len(arr) == 0:
        return collection
    
    if arr[0] % 2 == 0:
        collection.append(arr[0])
    
    return collection + even_numbers(arr[1:])


# print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def triangular_numbers(n):

    if n == 1:
        return 1
    
    return n + triangular_numbers(n - 1)


# print(triangular_numbers(6))


def index_of_x(str, index = 0):
    
    if str[0] == "x":
        return 0
    
    return 1 + index_of_x(str[1:])


print(index_of_x("abcdefghijklmnopqrstuvwxyz"))


