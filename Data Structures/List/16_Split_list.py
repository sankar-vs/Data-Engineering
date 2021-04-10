'''
@Author: Sankar
@Date: 2021-04-10 08:47:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 08:55:09
@Title : List_Python-16
'''
'''
Write a Python program to split a list based on first character of word.    
'''
from itertools import groupby
from operator import itemgetter

list = ['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And', 'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill', 'Billgone']
for letter, words in groupby(sorted(list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
    print("-----------------------------------")