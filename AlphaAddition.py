# Your task is to add up letters to one letter.
#
# The function will be given a variable amount of arguments,
# each one being a letter to add.
#
# Notes:
# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
# Examples:
# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'
def add_letters (*letters):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z']
    x = []
    total = 0

    if len(letters) == 0:
        return 'z'

    for v in letters:
        x.append(v)

    print (x.sort())

    for currValue in letters:
        total = total + alpha.index(currValue) + 1

    if total >= 25:
        total = total - 25

    return alpha[total - 1]

def main():
    print(add_letters ('b','z','a'))

if __name__ == '__main__':
    main()



