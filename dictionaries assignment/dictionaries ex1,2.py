'''
Thursday 15 October 2026
Mustapha
Dictionary exercises Q1 + 2
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
sentence= input('Enter a sentence: ')
sentence= sentence.upper()
words= sentence.split()
chars= sorted(sentence)

choice= input('Enter (word) for words and (char) for characters: ')
while True:
    if choice.upper()=='WORD':
        frequency(words)
        for k,v in dic.items():
            print(f'{k}--->{v}')
        break
    elif choice.upper()=='CHAR':
        frequency(chars)
        for k,v in dic.items():
            print(f'{k}--->{v}')
        break

    else:
        choice= input('Try again. Enter (word) for words and (char) for characters: ')

    


