# Sum of Pairs
# Given a list of integers and a single sum value, return the first two values
# (parse from the left please) in order of appearance that add up to form the sum.
#
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]

#def sum_pairs(ints, s):
def pairSum2(ints, s):

    if len(ints) < 2:
        return
    seen=set()
    output=set()

    for num in ints:
        target=s-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )

    return '\n'.join( map(str, list(output)) )


def main():
    ints = [2, 3, -5, 4, 9,10,7]
    print(pairSum2(ints, 19))

if __name__ == '__main__':
    main()
