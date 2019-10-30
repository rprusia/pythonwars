from functools import reduce

def get_average(marks):
    return int (reduce(lambda a,b: a + b, marks )/ len(marks))



def main():
    marks = [1,2,3,4,5,6,7]
    avg = get_average(marks)
    print(avg)

if __name__ == "__main__":
    main()

