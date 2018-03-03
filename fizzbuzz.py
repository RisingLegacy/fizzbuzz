def fizzbuzz(number):
    if number_divisible_by_three(number) and number_divisible_by_five(number):
        return 'fizzbuzz'
    elif number_divisible_by_three(number):
        return 'fizz'
    elif number_divisible_by_five(number):
        return 'buzz'
    return str(number)


def number_divisible_by_five(number):
    return number % 5 == 0

def number_divisible_by_three(number):
    return number % 3 == 0

