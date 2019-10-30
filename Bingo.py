# For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input.
# Duplicate numbers within the array are possible.
#
# Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc).
# Write a function where you will win the game if your numbers can spell "BINGO".
# They do not need to be in the right order in the input array). Otherwise you will lose.
#     Your outputs should be "WIN" or "LOSE" respectively.

def bingo(array):

    result = None
    bingo = [2, 9, 14, 7, 15]  # values of letters for bingo
    b = None
    i = None
    n = None
    g = None
    o = None
    gCounter = 0

    for num in array:
        if num in bingo:
           if num == 2:
               b = True
           elif num == 9:
               i = True
           elif num == 14:
               n = True
           elif num == 7:
               g = True
           elif num == 15:
               o = True

    if b and i and n and g and o:
        result = 'WIN'
    else:
        result = 'LOSE'

    return result

def main():
    arr = [1,2,3,7,5,14,7,15,9,10]
    print(bingo(arr))

if __name__ == '__main__': main()