
/*
Search space from 1 to the max val (except you keep track, not an array)
because with max val would get you the fastest eating, 
but we want the minimum eating rate k. thus bin search.
*/

#include <vector>
using namespace std;
class Solution {
    public:
    
        int eatBananas(vector<int>& piles, int k) {
            // return k;
            int hours = 0;
            for (int i = 0; i < piles.size(); ++i) {
                hours += (int) ceil((double) piles[i] / (double) k);
                cout << "HI" << (double) piles[i] / (double) k << endl;
            }
            cout << "k : " << k << " hours: "<<hours << endl; 
            return hours;
        }
    
        int binSearch(vector<int>& piles, int h, int l, int r, int min_k) {
            
            if (l > r) {
                cout << "oop" << endl;
                return min_k;
            }
    
            int mid = (l+r)/2;
            int hrs = eatBananas(piles, mid);
            if (hrs <= h) {
                // decrease eating speed
                min_k = mid;
                return binSearch(piles, h, l, mid-1, min_k);
            } else {
                // increase eating speed
                return binSearch(piles, h, mid+1, r, min_k);
            }
            
    
    
        }
    
        int minEatingSpeed(vector<int>& piles, int h) {
            vector<int> possible_k;
    
            // base case
            if (piles.size() ==1) return ceil( (double)piles[0] / h);
    
            // find max
            int max = piles[0];
            for (int i = 0; i < piles.size(); ++i) {
                max = std::max(piles[i], max);
            }
    
            // not needed
            // // populate search space for banana eating rates
            // for (int i = 1; i <= max; ++i ) {
            //     possible_k.push_back(i);
            // }
            
    
            int len = possible_k.size()-1;
            // binary search with possible k values from 1 to max value
            return binSearch(piles, h, 1, max, max);
    
        }
    };
    