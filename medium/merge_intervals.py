from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        srt = sorted(intervals, key=lambda x: x[0])

        merged.append(srt[0])
        i = 1
        while i < len(srt):
            last = merged.pop()

            # if current conflicts with last merged
            if last[1] >= srt[i][0]:
                if last[0] <= srt[i][0] and srt[i][1] <= last[1]:
                    merged.append(last) # do nothing -- in between
                if last[0] <= srt[i][0] and srt[i][1] > last[1]:
                    merged.append([last[0], srt[i][1]])
            else:
                merged.append(last)
                merged.append(srt[i])
            
            i += 1
            
        return merged


        