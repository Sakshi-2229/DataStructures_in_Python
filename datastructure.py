# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 03:08:20 2023

@author: sai
"""

"""python data structures
1. tuple - collection of objects. 
- it is immutable. 
- it is enclosed in ().
- cannot add or delete the value


2. list

3. dictionary

4. set
"""

#creating tuple
tup1 = (1, 2, 3, 4)
#Accessing elements of tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])


#tuples can hold different datatypes

tup2 = (1, 'John', True, -23.45)
print(tup2)




#iterating over tuples
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x)
    
#tuple related function
#you can also find out the length of tuple
len(tup3)
#you can count how many times a specified value appears 
#in a tuple

tup4=('apple','orange','plum','apple')
#tuples allows duplicates
tup4.count('apple')

#you can also find out the (first) index of a value in 
#a tuple:

tup4=('apple','orange','plum','apple','apple')
print(tup4.index('apple'))     #first occurrance index

print(tup4.index('plum'))

#checking if an element exists

if 'orange' in tup3:
    print('orange is in the tuple')
    

#holypython.com


#Nested tuples
#Tuples can be nested within tuples;
#that is a tuple can contain, as one of its
#elements, anothe tuple

tuple1 = (1,3,5,7)
tuple2=('john','Denis','phoebe','Adam')
tuple3=(43, tuple1, tuple2, 5.5)
print(tuple3)

#it is not possible to add or remove elements from a tuple
#they are immutable



#2. List
""" 
- list are mutable.
- ordered, indexed, structured
- can accomodate heterogenous entities
- enclosed in square brackets []
"""

#creating lists
lst1=['john','Paul','George','Ringo']
#AS with tuples we can have nested lists and lists 
#containing different elements

lst1=[1,43.5, True]
lst2=['apple','orange',31]
root_list=['apple',lst1,lst2,'Denise']
print(root_list)

#Accessing elements from lists
lst1=['john','Paul','George','Ringo']
print(lst1[-1])

lst1[0]
lst1[-2]

#in NLP list is used extensively

#range in the list
lst1=['John','Paul','George','Ringo']
print('lst1[1]:', lst1[1])
print('lst1[-1]:', lst1[-1])
print('lst1[:3]:', lst1[:3])
print('lst1[1:]:', lst1[1:])

#########################################################

#operations on list
#Adding to a list

lst1=['John','Paul','George','Ringo']
lst1.append('Pete')     #append() add the element at the end of the list
print(lst1)

#you can also add all the items in a list
#to another list. there are several options
lst1=['John','Paul','George','Ringo']
lst1.extend(['Albert','Bob'])   #can add new list
print(lst1)

#inserting into a list 
a_list=['Adele', 'Madonna', 'cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)

#list concatenation

lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=lst1+lst2
print(lst3)

#Assignments
"""
1. take 5 numbers in a list and find out minimum of list
 and maximum of the list. 
2. take 5 strings in a list and make it reverse it
3. take 10 numbers in a list write script to search for 
value (search for value whether it is present or not)
4. take 10 numbers in the list insert some duplicate 
numbers write script to check/find duplicates
5. take vowels in the list and non vowels letters find out
the total number of vowels in the list 
 
"""


lst=[1,2,3,4,5]
min_ele, max_ele = lst[0], lst[0]
 
for i in range(len(lst)):
    if lst[i] < min_ele:
        min_ele = lst[i]
         
    if lst[i] > max_ele:
        max_ele = lst[i]
         
print('\nMinimum Element in the list is', min_ele)
 
print('\nMaximum Element in the list is', max_ele)

##################################################

lst=['apple','banana','orange','grapes','mango']
reverse = [i[::-1] for i in lst]
 
# printing result
print ("The reversed list is : "+ str(reverse))

########################################################


#removing from list
another_list=['apple','banana','mango','orange']
print(another_list)
another_list.remove('banana')
print(another_list)

"""
# the pop method
1. it remove element from list
2. however it differs from the remove(). 
3. removing from the list is used in web scrapping 
   applications.
4. in remove we have to give name of entity and in pop 
   we have to give index of an entity
   
# method in two ways:
1. it takes an index which is index of the item to remove from 
than the object itself

"""

#pop element from the list
another_list=['apple','banana','mango','orange']
print(another_list)
another_list.pop(1)
print(another_list)
 

#inserting into a list
another_list=['apple','banana','mango','orange']
print(another_list)
another_list.insert(1,'grapes')
print(another_list)

"""
#creating a set
1. dont allow duplicates
2. enclosed in curly braces
3. unordered.

"""
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

#when will run this code it will print apple and orange only once.

#accessing elements in the set 
for item in basket:
    print(item)

#adding item to sets
basket={'apple','orange','apple','pear','orange','banana'}
basket.add('apricot')
print(basket)

#if you want to add more than one item to a set you can use the update
#when you want to update in sets you need to pass elements in the form of list
basket={'apple','orange','apple','pear','orange','banana'}
basket.update(['apricote','mango','grape'])
print(basket)

#obtaining the length of a set
basket={'apple','orange','apple','pear','orange','banana'}
len(basket)


#obtaining the max and min values in a set
basket2={1,2,3,4,5}
print(min(basket2))
print(max(basket2))


#removing an item
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)


#set operations
s1={'apple','orange','banana'}
s2={'grapefruit','lime','banana'}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)


"""
#Dictionaries
1. A dictionary is a set of association
2. between a key and value that is unordered
3. changeable (mutable) and indexed.

"""

capitals = {'Maharashtra':'Mumbai',
            'Gujarat':'Ahmadbad',
            'UP':'Lakhnow',
            'Karnataka':'Banglore',
            'Andrapradesh':'Hyderabad'}
print(capitals)

#Accessing items via keys
print('capitals[Maharashtra]:', capitals['Maharashtra'])

#Adding a new entity

capitals['West_Bengal']='Kolkatta'
capitals

#changing a keys value
capitals['Gujarat']='Gandhinagar'
print(capitals)


#removing an entry
capitals.pop('WEst_Bengal')
print(capitals)

capitals.pop('Karnataka')
print(capitals)


#another way to remove entry
del capitals['UP']
print(capitals)

#iterating over keys
capitals = {'Maharashtra':'Mumbai',
            'Gujarat':'Ahmadbad',
            'UP':'Lakhnow',
            'Karnataka':'Banglore',
            'Andrapradesh':'Hyderabad'}
for states in capitals:                       #it will print only keys
    print(states, end=', ')

for states in capitals:            #it will also print values
    print(states, end=', ')
    print(capitals[states])
    

#values, keys and items

print(capitals.values())
print(capitals.keys())
print(capitals.items())


#Checking key membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)

#obtaining the length of dictionary
print(len(capitals))


#Dictionaries can have values in tuple
seasons={'summer': ('Feb','March','April','May'),
         'Rainy': ('June','July','August','Sept'),
         'Winter': ('October','November','December','January')}
print(seasons['Rainy'])
print(seasons['Rainy'][0])

"""
#Dictionary Methods
1. get() is useful method to access the value of a key 
in a dictionary.
2. duplicates are not allowed in dictionaries
3. dictionary cannot have 2 items with the same keys.
"""
print(capitals.get('UP'))
 
######################################

dict2 = {
    "brand": "Maruti",
    "Model": "Breeza",
    "year": 2021,
    "year": 2020
    }
print(dict2)

#loop through a dictionary, it will show only keys
for x in dict2:
    print(x)
#print all values in the dictionary, one by one
for x in dict2:
    print(dict2[x])


#write python program to add all the items in the list
def sum_list(sum_list):
    sum=0
    for x in sum_list:
        sum=sum+x
    return sum
print(sum_list([5,6,-8]))

########################################################    

#Write python program to multiply all the items in the list

def mul_list(mul_list):
    mul=1
    for x in mul_list:
        mul=mul*x
    return mul
print(mul_list([2,3,4]))

#####################################################
#write python program to get the largest number from a list

lst=[4,5,6,9,10,87]
print(max(lst))
    

##################################
#write python program to get the smallest number from a list
lst=[4,5,6,9,10,87]
print(min(lst))

"""
#write python program to count the number of string which 
satisfies the condition that the string length is 2 or more
and the first and last character are the same from a given
list of string. given a list
['abc','xyz','aba','1221']

"""

def match_words(words):
    count=0
    for word in words:
        if len(words) > 2 and word[0] == word[-1]:
            count+=1
    return count
print(match_words(['abc','xyz','1221','aba','aaaa','ababa']))
 

############################################################
"""   
write a python program to get a list, sorted in increasing 
order by the last element of the tuple from the given list 
of non-empty tuples. 
sample list : [(2,5), (1,2), (4,4), (2,3), (2,1)] 
expected Result : [(2,1), (1,2), (2,3), (4,4), (2,5)]

"""

def last(n):
    return n[-1]
def sort_list_last(tuples):
    result=sorted(tuples, key=last)
    return result
print(sort_list_last([(2,5), (1,2), (4,4), (2,3), (2,1)]))


#write a program to remove 

lst1 = [10,20,30,40,20,10,10,50,60,80,40]
st1 = set(lst1)
#since set removes duplicate items. hence list is converted to set
print(st1)
lst2=list(st1)
print(lst2)

#write python program to clone or copy a list

original_list=[10,22,44,23,4]
new_list = list(original_list)
print(original_list)
print(new_list)


"""
write python program to find the list of words that are longer 
than n from a given list of words

"""
def long_words(n, str):
  word_len = []
  txt = str.split(" ")
  for x in txt:
    if len(x) > n:
      word_len.append(x)
  return word_len
print(long_words(3, "The quick brown for jumps over the lazy dog"))



"""
write a python function that takes two lists and returns True 
if they have at least one common member

"""
def common_data(list1, list2):
  result = False
  for x in list1:
    for y in list2:
      if x == y:
        result = True
  return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


"""
write python program to calaculate difference between 
the two lists.

"""
lst1=[1,3,5,7,9]
lst2=[1,2,4,6,7,8]
diff1 = list


"""
#write python program to convert list of characters into a string
#used in NLP
#used in web scrapping technique
"""
s = ['a','b','c','d']
str1 = ''.join(s)
print(str1)


"""
#write python program to find the index of an item in a specified 
list.
#used in recommendation engine.

"""

num=[20,30,40,50]
print(num.index(40))


#write a program to append a list to the second list.

lst1=[1,2,3,0]
lst2=['Red','Green','Black']
final_list = lst1 + lst2
print(final_list)

#################################################################

#write a python script to add a key to a dictionary.
#sample Dictionary : {0: 10, 1:20}
#Excepted Result : {0: 10, 1: 20, 2: 30}

d={0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d)

############################################################

#another logic
d={0: 10, 1: 20}
print(d)
d[2]=30
print(d)

############################################################

'''
#Write a python script to concatenate the following dictionaries
#to create a new one.
sample Dictionary:
    dict1={1:10, 2:20}
    dict2={3:30, 4:40}
    dict3={5:50, 6:60}

expected result:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}    
    
'''
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
dict4 = {}
for d in (dict1, dict2, dict3) : dict4.update(d)
print(dict4)


#write python script to check whether a given key already exists 
#in a dictionary

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in a dictionary')
is_key_present(5)
is_key_present(9)

##################################################################

# write a python program to iterate over dictionaries using for loope.

d={'x':10, 'y':20, 'z':30}
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)

##################################################################
"""
#sorting Data  

#write a python script to add a key to a dictionary.
#sample Dictionary : {0: 10, 1:20}
#Excepted Result : {0: 10, 1: 20, 2: 30}

"""
d={0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d)

############################################################

#another logic
d={0: 10, 1: 20}
print(d)
d[2]=30
print(d)

############################################################

'''
#Write a python script to concatenate the following dictionaries
#to create a new one.
sample Dictionary:
    dict1={1:10, 2:20}
    dict2={3:30, 4:40}
    dict3={5:50, 6:60}

expected result:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}    
    
'''
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
dict4 = {}
for d in (dict1, dict2, dict3) : dict4.update(d)
print(dict4)


#write python script to check whether a given key already exists 
#in a dictionary

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in a dictionary')
is_key_present(5)
is_key_present(9)

##################################################################

# write a python program to iterate over dictionaries using for loope.

d={'x':10, 'y':20, 'z':30}
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)

##################################################################



