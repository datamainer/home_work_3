def odd_nums(finite_number):
    for numbers in range(1, finite_number+1):
        if numbers % 2 != 0:
            yield numbers


user_finite_number = int(input('enter the finite numbers: '))

odd_numbers = odd_nums(user_finite_number)
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
