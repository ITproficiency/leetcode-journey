class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str (x)
        list_1 = []
        list_2= []
        for i in range(len(x)):
            list_1.append(x[i])
        for n in range (len(x),0,-1):
            list_2.append(x[n-1])
        if list_1 == list_2:
            return True     
        else:
            return False
    