#Saturday 7 November 2026
#Mustapha


def rsum(i):
    if i == 1:
        return 1
    else:
        return 1/i + rsum(i-1)

x= int(input('Enter any positive integer: '))
print(round(rsum(x),2))
