#Saturday 7 November 2026
#Mustapha



def ssum(s):
    l= 0
    if len(s)== 0:
        return l
    else:
        return 1+ ssum(s[1:])
        

x= 'apples'
print(ssum(x))




