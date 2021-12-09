def solution(s):
    alpha = '-><'
    if all(char in alpha for char in s) and len(s) <= 100:
        list_of_s = list()
        list_of_s[:0]=s
        left = '<'
        right = '>'
        Counter=0
        for i in range(len(list_of_s)):
            if list_of_s[i] == right:
                list_s = list_of_s[i+1::]
                output = list_s.count(left)
                Counter+=output
    return 2*Counter


print(solution("<<<>>><<<>>>"))