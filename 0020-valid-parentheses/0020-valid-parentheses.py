class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 ==1:
            return False
        resource = {"(":")", "[":"]","{":"}"}
        checklist = []
        for i in range (len(s)):
            if s[i]in resource.keys():
                checklist.append(s[i])
            elif len(checklist) ==0:
                return False
            elif s[i] == resource[checklist[-1]]:
                checklist.pop()
            elif s[i]!= resource[checklist[-1]]:
                return False
        if len(checklist) !=0:
            return False
        return True