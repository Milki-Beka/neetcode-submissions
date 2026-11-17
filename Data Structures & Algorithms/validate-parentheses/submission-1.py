class Solution:
    def isValid(self, s: str) -> bool:
        ss=[]
        for i in s:
            if i=='(' or i == '{' or i == '[':
                ss.append(i)
            else:
                if ss==[]:
                    return False
                else:
                    top = ss.pop()   
                    if i == ')' and top != '(':
                        return False
                    if i == '}' and top != '{':
                        return False
                    if i == ']' and top != '[':
                        return False
        return len(ss) == 0