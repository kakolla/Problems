/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

 class Solution {
    public:
        bool canAttendMeetings(vector<Interval>& intervals) {
            sort(intervals.begin(), intervals.end(), 
            [](Interval a, Interval b) { 
                return a.start < b.start;
            
            });
            if (intervals.size() == 0) return true;
            int start = intervals[0].start;
            for (int i= 0; i < intervals.size(); ++i ) {
                if (intervals[i].start < start) return false;
                start += (intervals[i].end - intervals[i].start);
    
            }
            return true;
            
        }
    };
    