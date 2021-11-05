from ctypes import string_at
import string

def solution(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if all(char in alpha and char.islower() and not char.isspace() for char in s) and len(s) <= 200 and s.isalpha():
        list_of_s = list()
        list_of_s[:0]=s
        string_ = ''
        for i in range(len(list_of_s)):
            string_+=list_of_s[i]
            if len(list_of_s) == len(string_)*(s.count(string_)):
                return s.count(string_)
    else:
        return False

print(solution('abcabcabcabc'))