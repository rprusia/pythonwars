# What is in a name
# or rather, what's a name in? For us, a particular string is where
# we are looking for a name.
# Test weather or not the string contains all the letter which spell
# a given name in order

def name_in_str(str, name):
    pos = 0
    for currentChar in name.lower():
        if str.lower().find(currentChar,pos) == -1:
            # return False string is missing a character in name
            return False
        else:
            # char found store index
            pos = str.lower().find(currentChar, pos) + 1

    return True

def main():
    str = 'Just enough nice friends'
    name = 'Jennifer'
    print (name_in_str(str, name))


if __name__ == '__main__':
    main()