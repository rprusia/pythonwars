# In this Kata, you will be given a string that may have mixed uppercase and
# lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
#
# For example:
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()

def main():
    s = 'JJIJSasijjsss'
    x = solve(s)
    print(x)

if __name__ == '__main__': main()