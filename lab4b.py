#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    x= [l1 + l2]
    return(x)

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    intersect_list2 = []
    for element in l1:
        if element in l2:
            intersect_list2.append(element)
    return(intersect_list2)

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    intersect_list = []
    for element in l1:
        if element not in l2:
            intersect_list.append(element)
    for element in l2:
        if element not in l1:
            intersect_list.append(element)
    return(intersect_list)

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
