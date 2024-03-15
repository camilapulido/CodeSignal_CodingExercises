# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:10:18 2024

@author: Camila Pulido
"""

def FeedbackReview(feedback,size):
    import textwrap 
    return textwrap.wrap(feedback, width=size)

#%%

def isWordPalindrome(word):
    return word ==word[::-1]

#%%
def PermutationCipher(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)

#%%
