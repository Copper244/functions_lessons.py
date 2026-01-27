# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(numbers):
    for num in numbers
    if v < 0
    return False
    return True




# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(numbers):
    total = 0
    for num in numbers:
        if 0 < num < 1000:
            total += num
    return total

# Test list
numbers = [10, -5, 250, 1500, 0, 999, 42]

print(sum_less(numbers))   # Output: 10 + 250 + 999 + 42 = 1301





# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even(numbers):
    return sum(1 for x in numbers if x % 2 == 0)

    numbers = [1, 2, 3, 4,5]
