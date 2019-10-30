# Welcome. In this kata, you are asked to square every digit of a number.
#
# For example, if we run 9119 through the function, 811181 will come out,
# because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    strValue = str(num)
    list = []

    for value in strValue:
        a = pow(int(value), 2)
        list.append(str(a))
        b = ''.join(list)

    return b

def main():
    print(square_digits(9119))


if __name__ == "__main__":
    main()