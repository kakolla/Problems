"""
generate wildcards for a word and store those, it's just O(len_word)
i.e. store hello as *ello, h*llo, he*lo, ...
then search for these cards
"""
class MagicDictionary:

    def __init__(self):
        from collections import defaultdict
        self.word_map = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        # gen all possible ways we could change a letter
        for i in range(len(dictionary)):
            word = dictionary[i]
            for l in range(len(word)):
                to_search = word[:l] + "*" + word[l+1:]
                # print(to_search)
                self.word_map[to_search].append(word) # store

        

    def search(self, searchWord: str) -> bool:
        # handle case where searchWord = word in dict

        for i in range(len(searchWord)):
            to_search = searchWord[:i] + "*" + searchWord[i+1:]
            print(to_search)
            if to_search in self.word_map:
                # check if word != searchWord
                for m in self.word_map[to_search]:
                    if m != searchWord: return True

        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)