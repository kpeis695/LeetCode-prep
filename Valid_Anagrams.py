"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""
from collections import Counter
def isAnagram(s, t):
    return Counter(s)==Counter(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
s = "rat"
t = "car"
print(isAnagram(s, t)) 
""
