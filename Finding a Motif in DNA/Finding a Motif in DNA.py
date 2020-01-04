"""
Given two strings s and t, t is a substring of s if t is contained as a
contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found
to its left, including itself (e.g., the positions of all occurrences of
'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol
at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent
the starting and ending positions of the substring in s; for example,
if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note
that t will have multiple locations in s if it occurs more than once
as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""

from sys import argv

script, s, t = argv

#for char in s:
#    if char == t[0]:
"""
return_list = []
def check_recursive(s, t, s_index = 0, t_index = 0):

    #checks if t is a substring of s

    if (s_index + 1) == len(s):
        print("done")

    elif (s[s_index] == t[t_index]) and (t_index + 1 < len(t)):
        s_index += 1
        t_index += 1
        print('match start found')
        for t_ind in range(0, t_index + 1):
            check_recursive(s, t, s_index, t_ind)

    elif (s[s_index] == t[t_index]) and (t_index + 1 == len(t)):
        print('match start complete')
        return_list.append(s_index - t_index + 1)

    elif (s[s_index] != t[t_index]):
        print('no match')
        s_index += 1
        t_index = 0
        check_recursive(s, t, s_index, t_index)

    else:
        print('logic issue in code')


check_recursive(s, t)

"""

"""
#break up s into subunits that can be compared directly to t
def break_into_subunits(s, t):
    s_list = []
    subunit_s = []
    t_len = len(t)
    for char in s:
        #s_list.append(char)
"""

def subunit_check(s, t):
    len_t = len(t)
    len_s = len(s)
    subunit_s = []
    subunit_count = 0
    for subunit_index in range(0, len_s +1):
        if subunit_index + 1 + len_t - 1 <= len_s:
            subunit_s.append(s[subunit_index:subunit_index+len(t)])
            subunit_count += 1
        else:
            pass
    t_substring_positions = []
    for subunit_num in range(0, subunit_count + 1):
        if subunit_s[subunit_num - 1] == t:
            t_substring_positions.append(str(subunit_num))

    return ' '.join(t_substring_positions)


    #print(subunit_s)
    #print(subunit_count)
    #print(t_substring_positions)


print(subunit_check(s, t))
