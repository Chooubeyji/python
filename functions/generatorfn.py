#write a generator function that yields even numbers up to a specified limit
def even_numbers(limit):
    for i in range(2, limit+1, 2):
        yield i
for num in even_numbers(10):
    print(num)
#
# The generator function even_numbers yields even numbers up to a specified limit.
# The generator function even_numbers is defined with a single parameter limit.
# The even numbers are generated using a for loop that iterates over the range from 2 to limit+1 with a step of 2.
# The even numbers are yielded using the yield statement.
# The generator function even_numbers is called with a limit of 10.
# The even numbers up to the limit are generated and printed using a for loop.
# The generator function even_numbers can be used to generate even numbers up to any specified limit.
# The generator function even_numbers is defined using the yield statement to generate even numbers up to a specified limit.
# The even numbers are generated using a for loop that iterates over the range from 2 to limit+1 with a step of 2.
# The even numbers are yielded using the yield statement.