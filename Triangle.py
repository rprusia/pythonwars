def triangle(a, b, c):
    result = False;

    if (a + b) > c and (a + c) > b and (b + c) > a:
        result = True
    else:
        result = False

    return result

def main():
    triangle(1, 2, 2)

if __name__ == '__main__':
    main()