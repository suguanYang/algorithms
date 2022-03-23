# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
class Solution(object):
    letterMapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    def flat(self, arr):
        res = []
        def iter(curr, acc):
            if len(curr) == 0:
                return acc
            first = curr.pop(0)
            if isinstance(first, list):
                iter(first, acc)
            else:
                acc.append(first)
            iter(curr, acc)
        iter(arr, res)

        return res

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        combs = ['']
        for d in digits:
            letters = Solution.letterMapping[d]
            for i in range(len(combs)):
                mutlps = []
                for l in letters:
                    mutlps.append(combs[i] + l)
                combs[i] = mutlps
            combs = self.flat(combs)

        return combs

print(Solution().letterCombinations('23456'))
        