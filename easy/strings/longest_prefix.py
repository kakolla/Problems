from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        index = 0
        curr_letter = ""

        count = 0
        last_index_counted = -1
        while (index < len(strs[0])):
            print("index" + str(index))
            # check if empty string
            if len(strs[0]) == 0:
                index+=1
                continue
            curr_letter = strs[0][index] 
            for i in range(len(strs)):
                if index < len(strs[i]) and strs[i][index] == curr_letter:
                    count += 1


            if count == len(strs): # all of them share a letter
                if (index == last_index_counted + 1):
                    common += curr_letter
                    last_index_counted = index
            curr_letter = ""
            count = 0
            index += 1
        

        return common
                 
            


        
        