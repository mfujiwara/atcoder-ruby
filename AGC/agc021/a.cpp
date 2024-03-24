#include <bits/stdc++.h>
using namespace std;

int main() {
    string N;
    cin >> N;
    int sum = 0;
    for (int i=0;i<N.size();i++) {
        sum += N[i] - '0';
    }
    int ans = N[0] - '0' -1;
    ans += 9 * (N.size()-1);
    if (sum <= ans) {
        cout << ans << endl;
    } else {
        cout << sum << endl;
    }
}
