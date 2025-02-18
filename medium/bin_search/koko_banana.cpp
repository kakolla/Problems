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
    
        int binSearch(vector<int>& arr, vector<int>& piles, int h, int l, int r, int min_k) {
            
            if (l >= r) {
                cout << "oop" << endl;
                return min_k;
            }
    
            int mid = (l+r)/2;
            int hrs = eatBananas(piles, arr[mid]);
            if (hrs > h) {
                // increase eating speed
                return binSearch(arr, piles, h, mid+1, r, min_k);
            } else {
                // decrease eating speed
                min_k = arr[mid];
                return binSearch(arr, piles, h, l, mid, min_k);
            }
            
    
    
        }
    
        int minEatingSpeed(vector<int>& piles, int h) {
            vector<int> possible_k;
    
            // base case
            if (piles.size() ==1) return eatBananas(piles, piles[0]);
    
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
            int len = possible_k.size()-1;
            return binSearch(possible_k, piles, h, 0, len, possible_k[len]);
    
        }
    };
    