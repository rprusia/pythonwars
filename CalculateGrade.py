from functools import reduce

def betterThanAverage (classPoints, yourPoints):

    avg = reduce(lambda a, b: a + b, classPoints) / len(classPoints)

    if ( yourPoints > avg ):
        result = True
    else:
        result = False

    return result



def main():
    classpoints = [33, 55, 66, 77, 88, 99]
    betterThanAverage(classpoints, 92)

if __name__ == '__main__':
    main()