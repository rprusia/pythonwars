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

    lower_amount = 0
    upper_amount = 0

    for value in s:
        if (value.islower()):
            lower_amount = lower_amount + 1
        else:
            upper_amount = upper_amount + 1

    if lower_amount >= upper_amount:
        return s.lower()
    else:
        return s.upper()

def main():
    s = 'JJIJSasijjsss'
    x = solve(s)
    print(x)

if __name__ == '__main__': main()
