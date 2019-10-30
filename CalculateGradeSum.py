from functools import reduce

def betterThanAverage (classPoints, yourPoints):

   return yourPoints > sum(classPoints) / len(classPoints)


if __name__ == '__main__':
    main()