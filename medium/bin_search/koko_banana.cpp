// not solved
/*


Search space from 1 to the max val in the array 
because with max val in the array would get you the fastest eating, 
but we want the minimum eating rate k. thus bin search.
*/
#include <vector>


using namespace std;
class Solution {
    public:
    
        int eatBananas(vector<int>& piles, int h, int k) {
            int hours = 0;
            for (int i = 0; i < piles.size(); ++i) {
                hours += (piles[i]%k) + (piles[i]/k) ;
            }
            return hours;
        }
    
        int binSearch(vector<int>& arr, vector<int>& piles, int h, int l, int r, int min_k) {
            if (l > r) {
                cout << "oop" << endl;
                return min_k;
            }
    
            int mid = (l+r)/2;
            mid = arr[mid];
            int hrs = eatBananas(piles, h, mid);
            int hrs_min = eatBananas(piles, h, min_k);
            if (hrs < hrs_min) min_k = mid;
    
            // have to increase eating rate
            if (hrs > h) {
                return binSearch(arr, piles, h, mid+1, r, min_k);
            }
            else {
                // range of acceptable k, but have to find min
                // if a value of k every increases, stop as that's the min
                int new_mid = (l+mid)/2;
                new_mid = arr[mid];
                if (eatBananas(piles,h, new_mid) >= hrs_min) {
                    return mid;
                } else {
                    cout << "min k is" << min_k << endl;
                    return binSearch(arr, piles, h, l, mid, min_k);
                }
            }
    
    
        }
    
        int minEatingSpeed(vector<int>& piles, int h) {
            vector<int> possible_k;
    
            // find max
            int max = piles[0];
            for (int i = 0; i < piles.size(); ++i) {
                max = std::max(piles[i], max);
            }
    
            // populate search space for banana eating rates
            for (int i = 1; i <= max; ++i ) {
                possible_k.push_back(i);
            }
            
    
            // bin search
            int len = piles.size()-1;
            return binSearch(possible_k, piles, h, 0, len, possible_k[len]);
    
        }
    };
    