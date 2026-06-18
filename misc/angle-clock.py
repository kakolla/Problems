









class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour / 12 * 360 
        # minutes / 60 * 360
        hour_angle = hour / 12.0 * 360.0
        hour_angle += (minutes/60.0) *360/12
        min_angle = minutes / 60.0 * 360.0
        mx = max(hour_angle, min_angle)
        mn = min(min_angle, hour_angle)
        return min(mx-mn, 360.0 - (mx-mn))
        


        
