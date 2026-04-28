
#include <iostream>



using namespace std;
int main() {
	int t;
	cin >> t;

	int n;
	int ans;
	for (int i =0; i < t; i++) {
		cin >> n;
		if (n == 2) ans = 2;
		else if (n == 3) ans = 3;
		else if (n % 2 == 0) ans = 0;
		else ans = 1;
		cout << ans << '\n';	
	}




    return 0;
}
