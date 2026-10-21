'''
Thursday 15 October 2026
Mustapha
Dictionary exercises Q3
'''


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
        dic[val]= count
    return dic

dic= {}
lst= []
with open('book.txt','r') as file:
    for line in file:
        words= line.split()
        for i in words:
            if i in dic:
                dic[i]+= 1
            elif i not in dic:
               dic[i]= 1
           
           
def sorting(a):
    return a[1]
print(dic)
sorted_words= sorted(dic.items(),key= sorting, reverse=True)[:10]
print(dict(sorted_words))
            
        



