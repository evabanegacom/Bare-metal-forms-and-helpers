# def isPalindrome(s):
#     for idx in xrange(len(s)//2):
#         if s[idx] != s[len(s)-idx-1]:
#             return False
#     return True
 
# def palindromeIndex(s):
#     for idx in xrange((len(s)+1)//2):
#         if s[idx] != s[len(s)-idx-1]:
#             if isPalindrome(s[:idx]+s[idx+1:]):
#                 return idx
#             else:
#                 return len(s)-idx-1
#     return -1

def isPalindrome(s):
    for idx in range(len(s)):
        if s[idx] != s[len(s)-idx-1]:
            return False
    return True
 
s = 'madam'
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        if isPalindrome(s[:i]+s[i+1:]):
            pass

for i in range((len(s)+1)//2):
    m = s[:i]
    print(m)