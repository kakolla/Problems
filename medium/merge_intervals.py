class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # o: array of non-overlapping intervals
        # i: intervals, not sorted
        
        # sort based on start time
        intervals.sort(key=lambda x: x[0])

        st = []
        for s, e in intervals:
            if len(st) == 0:
                st.append([s, e])
                continue
            top = st.pop()
            a,b = top[0], top[1]
            if s <= b and e >= b:
                # merge
                st.append([a, e])
            elif s > b:
                st.append([a, b])
                st.append([s, e])
            else:
                st.append([a, b])
        
        return st