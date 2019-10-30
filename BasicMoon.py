def moon_weight(weight, increase, years):

    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s'  % (year, moon_weight))

def main():
    moon_weight(220, 1.25, 20)

if __name__ == '__main__': main()