"""
1 pointer in word, 1 pointer in abbrev
if you come across a digit, skip word pointer that many up
if pointers dont match same char, return False abbreviation

make sure to handle out of bounds falling with i
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # i: word, abbreviation
        # o: whether string matches given abbreviation

        i = 0 # word
        j = 0 # abbr
        num = 0
        while j < len(abbr):
            if abbr[j].isdigit():
                f = j
                if abbr[j] == '0':
                    return False
                # get whole number
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num = int(abbr[f:j])
                i += num # skip ahead this many
                if i > len(word):
                    return False # if we fall out
            else:
                # cur char is letter
                if i >= len(word) or abbr[j] != word[i]:
                    return False 
                i+= 1
                j+=1
        
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False