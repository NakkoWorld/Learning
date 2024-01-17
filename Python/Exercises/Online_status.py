'''
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
'''

#Function to count the online users in a dictionary
def online_count(statuses):
    #Create a list of lists with (key,value) of dictionary
    statuses_items = statuses.items()
    counter = 0
    #Loop to count the users
    for i,x in statuses_items:
        if x == "online":
            counter+=1
    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"}
online_members = online_count(statuses)
print(online_members)