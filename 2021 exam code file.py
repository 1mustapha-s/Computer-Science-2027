# Question 16(a)
# Examination Number: Mustapha

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
phrase= input('Enter a phrase: ')
ph= sorted(phrase.upper())

while ' ' in ph:
    ph.remove(' ')

print(ph)
wd1= word1.upper()
wd2= word2.upper()
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1.upper()) == sorted(word2.upper())):
    print(f'{word1} is an anagram of {word2}')
elif (sorted(word1.upper()) != sorted(word2.upper())):
    print(f'{word1} is not an anagram of {word2}')

if is_anagram(wd1,wd2):
    print(f'{word1} is an anagram of {word2}')
elif not is_anagram(wd1,wd2):
    print(f'{word1} is not an anagram of {word2}')
    
    
    
if ph == sorted(wd1):
    print(f'{word1} is an anagram of {phrase}')
elif ph != sorted(wd1):
    print(f'{word1} is not an anagram of {phrase}')
    
if ph == sorted(wd2):
    print(f'{word2} is an anagram of {phrase}')
elif ph != sorted(wd2):
    print(f'{word2} is not an anagram of {phrase}')