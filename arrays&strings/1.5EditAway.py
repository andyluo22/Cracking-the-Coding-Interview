# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away

# EXAMPLE: pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
import unittest
import time

# Good idea but doesn't take into account every edge case
# Some very similar words could be multiple edits away
# Should handle each case specifically 

def one_or_less_edits_away_incorrect(s1: str, s2: str) -> bool:
    char_table_one = [0] * 256
    char_table_two = [0] * 256
    
    largest_length = max(len(s1), len(s2))

    
    for char in s1:
        char_table_one[ord(char)] += 1
    
    for char in s2:
        char_table_two[ord(char)] += 1
        
    result = [a & b for a, b in zip(char_table_one, char_table_two)]

    count_non_zeros = sum(1 for element in result if element != 0)
    
    return abs(count_non_zeros - largest_length) <= 1    
    
def one_or_less_edits_away(s1: str, s2: str) -> bool:

    if len(s1) == len(s2):
        return same_length_edit_away(s1,s2)
    if len(s1) + 1 == len(s2):
        return one_length_edit_away(s1,s2)
    if len(s1) == len(s2) + 1: 
        return one_length_edit_away(s1,s2)
    
    return False

def same_length_edit_away_harder(s1: str, s2:str) -> bool:
    list1, list2 = list(s1), list(s2)
    
    mask = [a & b for a,b in zip(list1,list2)]
    
    count_non_zeros = sum(1 for element in mask if element != 0)
    
    return count_non_zeros <= 1

def same_length_edit_away(s1: str, s2: str) -> bool:
    edited: bool = False
    
    for c1, c2 in zip(s1,s2):
        if c1 != c2:
            if edited:
                return False
            
            edited = True
    
    return edited 

def one_length_edit_away(s1: str, s2: str) -> bool:
    i, j: int = 0
    edited: bool = False
    
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            
            i += 1
        else:
            i += 1
            j += 1
            
    return True