#include <bits/stdc++.h>
using namespace std;

int main() {
    int L,R;
    cin >> L >> R;
    vector<int> memo(41,0);
    for (int i=0;i<L;i++) {
        int l;
        cin >> l;
        memo[l]++;
    }
    int ret = 0;
    for (int i=0;i<R;i++) {
        int r;
        cin >> r;
        if (memo[r] > 0) {
            memo[r]--;
            ret++;
        }
    }
    cout << ret << endl;
}
