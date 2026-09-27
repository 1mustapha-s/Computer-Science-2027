'''
Mustapha
Friday 25 September 2026
Functions Revision
'''



def mean(a):
    m = sum(a)/ len(a)
    return m




def median(b):
    b.sort()
    if len(b)%2==0:
        m = ((len(b)//2)+ (len(b)//2)+1)//2
    else:
        m= len(b)//2
    m= b[m]
    return m




def mode(c):
    ulst= []
    count= 0
    val= 0
    mod= 0
    for i in c:
        if i not in ulst:
            ulst.append(i)
    for j in ulst:
        val= j
        count= c.count(j)
        if count > c.count(mod):
            mod = val
        elif count < c.count(mod):
            pass
    return mod
        

    


def frequency(d):
    ulst= []
    count= 0
    val= 0
    for i in d:
        if i not in ulst:
            ulst.append(i)
    for j in ulst:
        count= d.count(j)
        val= j
        print(f'Value:{val} Frequency:{count}')
    
        


def rang(e):
    r= max(e)-min(e)
    return r
