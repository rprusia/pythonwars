# What is in a name
# or rather, what's a name in? For us, a particular string is where
# we are looking for a name.
# Test weather or not the string contains all the letter which spell
# a given name in order

def name_in_str(str, name):
    it = iter (str.lower())
    return all(c in it for c in name.lower())

def main():
    str = 'Just enough nice friends'
    name = 'Jennifer'
    print (name_in_str(str, name))


if __name__ == '__main__':
    main()