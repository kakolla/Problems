














using namespace std;

class Solution {
public:
    double angleClock(int hour, int minutes) {
	    double hour_angle = hour / 12.0 * 360;
	    double min_angle = minutes / 60.0 * 360;
	    hour_angle += (minutes/60.0) * 360.0/12;

	    double mx = max(hour_angle, min_angle);
	    double mn = min(hour_angle, min_angle);
	    return min(mx - mn, 360.0 - (mx - mn));
	

        
    }
};
