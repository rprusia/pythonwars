def enum1():

    myList = ['one', 'two', 'three', 'four']
    for counter, value in enumerate(myList):
        print(counter, value)

def enum2():
    myList = ['apple', 'pear', 'peach', 'banana']
    for c, value in enumerate(myList, 2):
        print(c, value)

def enum3():
    myList = ['apple', 'pear', 'peach', 'banana']
    counter_list = list(enumerate(myList, 1))  # creates a tuple
    print(counter_list)

def main():
    enum1()
    print('\n')
    enum2()
    print('\n')
    enum3()

if __name__ == '__main__': main()


