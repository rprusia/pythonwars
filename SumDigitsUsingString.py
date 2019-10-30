def sumDigits(number):
    return sum( int(d) for d in str(abs(number)))

def main():
    x = sumDigits(120)
    print(x)

if __name__ == '__main__': main()
