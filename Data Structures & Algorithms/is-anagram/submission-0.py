class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap_s = {}
        hashmap_t = {}

        for string in s:
            if string not in hashmap_s:
                # HashMap1[char] = text1.count(char)
                hashmap_s[string] = s.count(string)

        for string in t:
            if string not in hashmap_t:
                # hashmap_t.add(string, t.count(string))
                hashmap_t[string] = t.count(string)

        if hashmap_s == hashmap_t:
            return True


        return False 
        