class Solution:
    def calculate(self, exp):
        inputs = []
        acc = 0
        stack = []
        digit = 0

        def getOperators(s):
            acc = ''
            for i in range(len(s)):
                if s[i].isdigit():
                    acc += s[i]
                else:
                    return {
                        'val': int(acc),
                        'pos': i - 1
                    }
            return {
                'val': int(acc),
                'pos': i
            }

        def iter(s):
            if len(s) == 0:
                return
            curr_s = s[0]
            if curr_s.isdigit():
                res = getOperators(s)
                stack.append(res.get('val'))
                iter(s[res.get('pos') + 1:])
            elif curr_s == '+':
                s = s[1:]
                res = getOperators(s)
                stack.append(res.get('val'))
                iter(s[res.get('pos') + 1:])
            elif curr_s == '-':
                s = s[1:]
                res = getOperators(s)
                stack.append(-res.get('val'))
                iter(s[res.get('pos') + 1:])
            elif curr_s == '*':
                s = s[1:]
                res = getOperators(s)
                stack.append(stack.pop() * res.get('val'))
                iter(s[res.get('pos') + 1:])
            elif curr_s == '/':
                s = s[1:]
                res = getOperators(s)
                stack.append(stack.pop() // res.get('val'))
                iter(s[res.get('pos') + 1:])

        iter(exp)
        return sum(stack)


print(Solution().calculate('3*2/5'))