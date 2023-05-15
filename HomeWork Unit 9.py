#9.1  Define a function called good() that returns the list ['Harry', 'Ron', 'Hermione']
def good():
    return ['Harry','Ron','Hermione']

print(good())

# Help me (9,2; 9,3;)!!!!!!! ----Google helped...

#9.2
#Define a generator function called get_odds that returns the odd numbers from
# range(10). Use a for loop to find and print the third value returned.
limit = 10
get_odds = (num for num in range(limit) if not num % 2 == 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1



# def get_odds():
#     for number in range(1, 10, 2):
#         yield number

# count = 1
# for number in get_odds():
#     if count == 3:
#         print("The third odd number is", number)
#         break
#     count += 1

#9.3
#  Define a decorator called test that prints 'start' when a function is called and
# 'end' when it finishes.


def test(func):
    def nested_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return nested_function

@test
def add(a, b):
    print(a + b)

add(12,4)

# 9.4 Define an exception called OopsException. Raise this exception to see what hap‐
# pens. Then write the code to catch this exception and print 'Caught an oops'.


class OopsException(Exception):
    pass
def with_exception(a):
    if a < 0:
        raise OopsException(a)
try:
    with_exception(-1)
except OopsException as exc:
    print('Caught an oops')
#1