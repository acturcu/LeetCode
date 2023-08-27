class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        while len(a) and len(b):
            l = a[-1]
            r = b[-1]
            if l == '1' and r == '1' and carry == 0:
                res += "0"
                carry = 1 
            elif l == '1' and r == '1' and carry == 1:
                res += "1"
            elif l == '1' and r == '0' or r == '1' and l == '0':
                if carry == 0:
                    res += "1"
                else:
                    res += "0"
                    
            else:
                res += str(carry)
                carry = 0
            a = a[:len(a) - 1]
            b = b[:len(b) - 1]
        
        while len(a):
            l = a[-1]
            if l == '1' and carry == 1:
                res += "0"
            elif l == '1' and carry == 0:
                res += "1"
            elif l == '0' and carry == 1:
                res += "1"
                carry = 0
            else:
                res += "0"
            a = a[:len(a) - 1]
        
        while len(b):
            l = b[-1]
            if l == '1' and carry == 1:
                res += "0"
            elif l == '1' and carry == 0:
                res += "1"
            elif l == '0' and carry == 1:
                res += "1"
                carry = 0
            else:
                res += "0"
            b = b[:len(b) - 1]
        
        if carry :
            res += "1"
        
        return res[::-1]