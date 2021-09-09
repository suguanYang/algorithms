import sys

inputs = ''
for line in sys.stdin:
    line = line.replace('\n', '')
    if len(line) == 0:
        break
    inputs = line

syb_mapping = {
    '{': '}',
    '[': ']',
    '(': ')'
}

class Solution:
    def getBanlancedSymbol(self, exp, syb):
        acc = ''
        banlanced = 1
        for i in range(len(exp)):
            if exp[i] == syb:
                banlanced += 1
            if exp[i] == syb_mapping.get(syb):
                banlanced -= 1 
            if banlanced == 0:
                return {
                    'exp': acc,
                    'pos': i
                }
            else:
                acc += exp[i]
                
        return None

    def calculate(self, exp):
        num = 0
        stack = []
        preIns = '+'
        exp = exp + '@'
        while exp != '':
            s = exp[0]
            rest = exp[1:]
            if s.isdigit():
                num = num * 10 + int(s)
            else:
                if s == '{':
                    res = self.getBanlancedSymbol(rest, '{')
                    num = self.calculate(res.get('exp'))
                    rest = rest[res.get('pos')+1:]
                if s == '[':
                    res = self.getBanlancedSymbol(rest, '[')
                    num = self.calculate(res.get('exp'))
                    rest = rest[res.get('pos')+1:]
                if s == '(':
                    res = self.getBanlancedSymbol(rest, '(')
                    num = self.calculate(res.get('exp'))
                    rest = rest[res.get('pos')+1:]
                if preIns == '+':
                    stack.append(num)
                elif preIns == '-':
                    stack.append(-num)
                elif preIns == '*':
                    l = stack.pop()
                    stack.append(l * num)
                elif preIns == '/':
                    l = stack.pop()
                    stack.append(l / num)

                num = 0
                preIns = s
            exp = rest
        
        return int(sum(stack))
print(Solution().calculate(inputs))

# print(Solution().getBanlancedSymbol('2+3)', '('))