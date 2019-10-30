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
    
    if not letters: 
        return 'z'

    return chr(ord('a') + (sum(map(lambda char:ord(char)-ord('a')+1 , letters))-1)%26)
  
def main():
    print(add_letters ('b','z','a'))

if __name__ == '__main__':
    main()



