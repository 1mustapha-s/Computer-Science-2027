#Saturday 7 November 2026
#Mustapha




def lsum(l):
    s=0
    if len(l)== 0:
        return s
    else:
        s+= l[0] + lsum(l[1:])
        return s

x= [1,2,3,4,5]
print(lsum(x))