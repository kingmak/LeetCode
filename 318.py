class Solution(object):
    def maxProduct(self, words):
        lenMap = {}
        for word in words:
            lenMap[word] = len(word)
            
        sort = sorted(lenMap, key = lenMap.get)[::-1]
        pairs = []

        i = 0
        while i < len(sort):
            j = 0
            while j < len(sort):
                if len(sort[j]) == len(sort[i]):
                    if i != j: # comparison here as its a 1 time per loop so less comparisons will be made
                        for char in sort[j]:
                            if char not in sort[i]:
                                if sort[j] not in pairs: # fix this 
                                    pairs.append(sort[j])
                                break
                j += 1
            i += 1

        i = 0
        length = 0
        while i < len(pairs) - 1:
            for char in pairs[i]:
                gold = True
                if char in pairs[i + 1]:
                    gold = False
                    break
            if gold:
                length = len(pairs[i]) * len(pairs[i + 1])
                break
            i += 1
            
        if length < 0:
            return 0
        return length

                
tests = [
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
            ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
            ["a", "aa", "aaa", "aaaa"],
            ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"] # should be 15
        ]

sol = Solution()
for test in tests:
    print sol.maxProduct(test)
