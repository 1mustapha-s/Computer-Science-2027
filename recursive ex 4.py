#Saturday 7 November 2026
#Mustapha#



def nsum(n):
    if n== 0:
        return 0
    else:
        if n%2 == 0:
            return nsum(n-1)
        elif n%2 != 0:
            return n + nsum(n-1)


        

x= int(input('Enter a number: '))
print(nsum(x-1))


