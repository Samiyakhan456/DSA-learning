class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char,0)+1
        for char in t:
            count_t[char] = count_t.get(char,0)+1
        return count_s == count_t
       # The get() method in Python is used to retrieve the value of a specified key from a dictionary. 

        
# Alternative solution without using get() method
count_s = {}
for char in s:
    if char in count_s:
        count_s[char] = count_s[char] + 1
    else:
        count_s[char] = 1
count_t = {}
for char in t:
    if char in count_t:
        count_t[char] = count_t[char] + 1
    else:
        count_t[char] = 1
return count_s == count_t:
    