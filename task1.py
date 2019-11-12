# Program that accepts multiple number of sentences as input and
# prints the lines after making all characters in the sentence capitalized.

st = input('Enter the string  : ')
out = ''
for n in st:
    if n not in 'abcdefghijklmnopqrstuvwqxyz':
        out = out + n
    else:
        k = ord(n)
        l = k - 32
        out = out + chr(l)
print()
print(out) 