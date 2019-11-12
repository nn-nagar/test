#           2(rebbit + chicken) = heads
#            4rebbit + 2chicken = legs
#          -        -
#          -----------------------------
#             2rebbit = legs - 2heads

#           r = (legs - 2heads)/2

heads = int(input('Enter the total number of heads :  '))
legs = int(input('Enter the total number of legs :   '))

if (legs%2!=0):
    print('----------no solution-------------')

elif (heads==0):
    print('----------no solution-------------')

elif (heads>legs):
    print('----------no solution-------------')

else:
    rebbit=int((legs+(-2*heads))/2)
    chicken= int(heads - rebbit)
    print('{} {}'.format(chicken,rebbit))

