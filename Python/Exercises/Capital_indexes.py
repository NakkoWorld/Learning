'''
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

#Function to get a list of the indexes that have capital letters.
def capital_indexes(word):
    #We enumerate the word to get the word and the value separated.
    enumerated_word = enumerate(word)
    #List to return
    final_list = []
    #Loop to check if the letter is upper and then append the index.
    for index, letter in enumerated_word:
        if letter.isupper():
            final_list.append(index)
    return final_list


listed_indexes = capital_indexes("HeLlO")
print(listed_indexes)