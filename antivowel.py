import re

def anti_vowel(text):
        newtext = re.sub('[AEIOUaeiou]', '', text)
        print newtext

anti_vowel("Hey Look Words!")
anti_vowel("THE QUICK BROWN FOX SLYLY JUMPED OVER THE LAZY DOG")