#Saturday 7 November 2026
#Mustapha



def nsum(n):
    s= 0
    if len(n)== 0:
        return s
    else:
        return int(n[0])+ nsum(n[1:])
        
x= '17'
print(nsum(x))






