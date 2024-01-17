'''
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''
#Function to get the middle letter of a string.
def mid(word):
    word_length = len(word)
    #Conditional to check if the word has pair letters
    if word_length % 2 == 1:
        #Return the middle letter calculating the index of the middle letter.
        letter_num = int(word_length/2)
        return word[letter_num]
    else: return ""

mid_letter = mid("abc")
print(mid_letter)