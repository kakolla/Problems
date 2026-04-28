
#include <iostream>
#include <vector>


using namespace std;



vector<int> run(int n, vector<int>& a, vector<int>& b, int l, int r) {
	// swap b with a (max)
	int i;

	for (i =0 ; i < n; i++) {
		if (b[i] > a[i]) {
			a[i] = b[i];
		}
	}
	// right to left, swap if better
	for (i = n-1; i > 0; i--) {
		if (a[i] > a[i-1]) a[i-1] = a[i];
	}


	// prefix sum arr
	vector<int> pref;
	int prev = 0;
	for (int i= 0; i < n; i++ ){
		prev += a[i];
		pref.push_back(prev);
	}
	return pref;

}
int run_query(vector<int>& prefs, int l, int r) {
	int r_sum = prefs[r-1];
	int l_sum;
	if (l-1 == 0) l_sum = 0;
	else l_sum = prefs[l-2];
	
	return r_sum - l_sum;
}

int main() {
	int t, n, q;
	vector<int> a;
	vector<int> b;
	cin >> t;
	vector<int> ans;
	for (int j= 0; j < t; j++) {
		cin >> n >> q;
		int temp;
		for (int i =0; i < n; i++) {
			cin >> temp;
			a.push_back(temp);
		}
		for (int i =0; i < n; i++) {
			cin >> temp;
			b.push_back(temp);
		}
		int l,r;
		vector<int> prefs = run(n, a, b, l, r);
		for (int i =0; i< q; i++) {
			cin >> l >> r;
			ans.push_back(run_query(prefs, l, r));
		}
		for (auto& e : ans) cout << e << " ";
		cout << endl;
		ans.clear();
		a.clear();
		b.clear();
	
	}



    return 0;
}
