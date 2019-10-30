first_name = 'ray'
last_name = 'jones'
full_name = f"{first_name} {last_name}"   # example of f-string, placing 'f' before string values

print (full_name)
print(f"Hello, {full_name.title()}")  # f-string

# special chars
print('\tRay \nPrusia \t123')

# strip white space - rstrip

value = 'Ray '
print(value.rstrip())    # strip from right side
value = ' ray '
print(value.lstrip())

# simple message
name = 'Eric'
print (f'Hello are you ready to learn stuff {name}')  # string

caseName = 'RaY pruSia'
print(caseName.lower())
print(caseName.upper())
print(caseName.title())

name = 'Albert Einstein'
value = 'A person who never made a mistake never tried anything'
print(f'{name} said: \"{value}\"')
