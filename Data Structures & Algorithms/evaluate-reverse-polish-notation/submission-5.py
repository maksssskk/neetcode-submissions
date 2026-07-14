class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = ['+', '-', '*', '/']
        stack = []

        for c in tokens:
            if c not in opers:
                stack.append(int(c))
            else:
                f = stack.pop()
                s = stack.pop()
                if c == '+':
                    res = f + s
                elif c == '-':
                    res = s - f
                elif c == '*':
                    res = f * s
                else:
                    res = int(s/f)
                stack.append(res)
        return int(stack[0])