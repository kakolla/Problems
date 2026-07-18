#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

#include <unordered_map>


using namespace std;

class Solution {
public:
	vector<string> ans;
	void dfs(string node, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& adj) {

		while (!adj[node].empty()) {
			string nei = adj[node].top();
			adj[node].pop();
			dfs(nei, adj);
		}
	
		ans.push_back(node);


	}

	vector<string> findItinerary(vector<vector<string>>& tickets) {
		ans.clear();

	    // create adj list
	    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;

	    for (auto& e : tickets) {
		    // connection
		    adj[e[0]].push(e[1]);
	    }


	    for (auto& [k,v] : adj) {
		    cout << k << ": ";
		    cout << v.top() << endl;
	    }

	    dfs("JFK", adj);


	    reverse(ans.begin(), ans.end());
	    return ans;


        
    }
};
