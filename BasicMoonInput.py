import sys

def moon_weight():
    print('Enter starting weight')
    weight = int(sys.stdin.readline())
    print('Enter in years')
    years = int(sys.stdin.readline())
    print("Enter yearly increase" )
    increase = int(sys.stdin.readline())


    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s'  % (year, moon_weight))

def main():
    moon_weight()

if __name__ == '__main__': main()