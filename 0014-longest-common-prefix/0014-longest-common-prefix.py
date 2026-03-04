class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result =""
        shortest_str = min(strs,key = len)
        if shortest_str == "":
            return ""
        for m in range (len(shortest_str)):
            condition = True
            for n in range (len(strs)):
                if shortest_str[m] != strs[n][m]:
                    condition = False
                    return (result)
            if condition == True:
                result+= shortest_str[m]
        return(result)
