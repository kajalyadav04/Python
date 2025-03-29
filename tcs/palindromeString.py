class Solution(object):
    def isPalindrome(self, s):
         k="".join(char.lower() for char in s if char.isalnum())
         return k==k[::-1]
    def isPalindromeNum(self, s):
        k=""
        for char in s:
            if char.isalnum():
                k+= char.lower()

        if k=="":
            return True

        reverse_str=""
        for i in range(len(k)-1,-1,-1):
            reverse_str+=k[i]
        return reverse_str==k