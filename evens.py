def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the funciton"
    if numbers is empty return false
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the number of even numbers is even, return True
    """

    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        return True if evens and evens % 2 == 0 else False
        
        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False

    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 4]))