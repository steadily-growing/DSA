class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       for i in s:
            if i == '(' or i == '[' or i == '{':
               stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if (i == ')' and top == '(') or \
                       (i == ']' and top == '[')or \
                       (i == '}' and top == '{'):
                       continue
                    else:
                        return False
       if len(stack) == 0:
            return True
       else:
            return False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { ")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        