class Solution:
    def romanToInt(self, s: str) -> int:
        roman ={"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        value = 0
        i = 0
        while i < len(s):
            if i < len(s)-1:
                current_value = roman[s[i]]
                next_value = roman[s[i+1]]
                if current_value < next_value:
                    extra = next_value - current_value
                    value += extra
                    i+=2
                if current_value >= next_value:
                    extra = current_value
                    value += extra
                    i+=1
            if i == len(s)-1:
                value+= roman[s[i]]
                i+=1
        return(value)
    