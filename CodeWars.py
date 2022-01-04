#################### Welcome to functions 
# ####1
#Write a function that takes an integer as input
# , and returns the number of bits that are equal
#  to one in the binary representation of that number
# . You can guarantee that input is non-negative.
def count_bits(n):
    temp = format(n,'b')
    print(temp)
    counter=0
    for x in temp:
        if x == '1':
            counter+=1
           
    return counter
 ####2
 #  Implement the function which takes an array containing the names of people that like an item. 
 # It must return the display text as shown in the examples
 #   You probably know the "like" system from Facebook 
 # and other pages. People can "like" blog posts
 # , pictures or other items. We want to create the text 
 # that should be displayed next to such an item

def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif  len(names)==1:
        return names[0]+' likes this'   
    elif len(names)==2:
            return names[0]+' and '+names[1]+' like this'
    elif len(names)==3:
        return names[0]+', '+names[1]+' and '+names[2]+' like this'
    else:
        result = names[0]+', '+names[1]+' and '
        counter=0
        while counter<len(names)-2:
              counter+=1
        result+=str(counter)+' others like this' 
        return result
####3
#A Narcissistic Number is a positive number which is 
# the sum of its own digits, each raised to the power of 
# the number of digits in a given base. In this Kata
# , we will restrict ourselves to decimal (base 10).

def narcissistic( value ):

    num_digits=0
    temp =value
    while temp>0:
        num_digits+=1
        temp/=10
        temp=int(temp)
    i=0 
    temp =int(value)
    narciss_num=0
    temp=value
    while i<num_digits:
        narciss_num+=((temp%10)**num_digits)
        temp/=10
        temp=int(temp)
        print(i,narciss_num)
        i+=1
    print(narciss_num)
    if value==narciss_num:
        return True
    else:
        return False
    
####4
#Move the first letter of each word to the end of it
# , then add "ay" to the end of the word.
#  Leave punctuation marks untouched.
import string
def pig_it(text):
    list_text = text.split()
    
    return ' '.join([ word if word in string.punctuation 
    else word[1:]+word[0]+'ay' for word in list_text])
    


####5
#The goal of this exercise is to convert a string to a new string
#  where each character in the new string is 
# "(" if that character appears only once in the original string,
#  or ")" if that character appears more than once in the original string.
#  Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    new_word=''
    i=0
    word=word.lower()
    print(word)
    while i<len(word):
        if i==0:
            temp=word[1:]
        else:
            temp=word[0:i]+word[i+1:]
        if word[i] in temp:
            new_word+=')'
        else:
            new_word+='('
        i+=1    
 
    return new_word    
print(duplicate_encode('Hello'))