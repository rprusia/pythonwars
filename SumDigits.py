# Write a function named sumDigits which takes a number as input and
# returns the sum of the absolute value of each of the number's decimal digits.
#
# For example:
# sumDigits(10)  # Returns 1
# sumDigits(99)  # Returns 18
# sumDigits(-32) # Returns 5

def sumDigits(number):

    total = 0
    number = abs(number)
    while (number > 0):
        dig = number % 10
        total = total + dig
        number = number // 10

    print(f"Total:  {total}")

    return total


def main():
     x = sumDigits(120)
     print(x)

if __name__ == '__main__': main()


