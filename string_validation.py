'''You are given a string .
Your task is to find out if the string  contains:
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.'''

s = input()
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
        ''' i is iterated bcz these fun take char by char '''
        
    '''Python, any() is a built-in function that takes an iterable
(such as a list, tuple, set, or any other iterable object) as its argument
and returns True if at least one element in the iterable evaluates to True.
If all the elements in the iterable are falsy, the any() function returns False.'''