# difficulty: Medium
# Runtime: 181 ms, faster than 42.92% of Python3 online submissions for Longest Word in Dictionary.
# Memory Usage: 14.4 MB, less than 72.42% of Python3 online submissions for Longest Word in Dictionary.

class Solution:
    def longestWord(self, words: List[str]) -> str:
        l = 0
        ans = ''

        trie = {}

        words.sort()

        for word in words:
            node = trie
            cnt = 0
            prev = True

            if len(word) == 1:
                if word not in trie:
                    cnt = 1
                    trie[word] = {}
            else:
                for c in word:
                    if c in node:
                        node = node[c]
                        cnt += 1
                    elif cnt+1 == len(word):
                        cnt += 1
                        node[c] = {}
                    else:
                        cnt = 0
                        break

            if l < cnt:
                l = cnt
                ans = word

        return ans
