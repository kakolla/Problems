class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # i: list of intervals
        # o: min number of rooms needed
        
        # first sort on start times
        intervals.sort(key=lambda x: x[0])

        # use min heap to store earliest end time for a room
        import heapq
        earliest_end_time = []

        rooms = 0
        for s, e in intervals:
            if len(earliest_end_time) == 0:
                earliest_end_time.append(e)
                rooms += 1
                continue
            
            # check earliest end time of a room for conflicts
            top = earliest_end_time[0]
            if s < top:
                rooms += 1
                heapq.heappush(earliest_end_time, e)
            else:
                # remove previous meeting
                heapq.heappop(earliest_end_time)
                heapq.heappush(earliest_end_time, e)
        
        return rooms
    