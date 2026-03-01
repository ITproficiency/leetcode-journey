class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0   
        if x== 0 or 0 < x < 10 :
            return True
        if x <0 :
            return False
        if x % 10 == 0 :
            return False    
        while x > reversed:
            reversed = reversed*10 + int(x%10)
            x= x//10
        if x == reversed//10 or x == reversed:
            return True
        return False