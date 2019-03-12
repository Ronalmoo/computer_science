class Solution:
    def longestCommonPrefix(self, strs):
        result = ''
        for x in zip(*strs):
            if len(set(x))==1:
                result +=list(set(x))[0]
            else:
                break
        return result

answer = Solution()
print(answer.longestCommonPrefix(['flower', 'flame', 'floor']))




