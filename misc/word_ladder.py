









class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        



        from collections import deque



        words = set(wordList)


        # hot, hit
        # hot, hit

        curr = beginWord
        q = deque()
        q.append((curr, 1))

        visited = set()

        while q:
            curr, steps = q.popleft()
            print(curr)
            for i in range(len(curr)):
                new = curr
                for j in range(26):
                    new = new[:i] + chr(97 + j) + new[i+1:]
                    if new in words and new == endWord:
                        return steps+1
                    if new in words and new not in visited:
                        visited.add(new)
                        q.append((new, steps+1))

        return 0








