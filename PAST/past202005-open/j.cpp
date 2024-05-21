#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> memo(N);
    int a;
    for (int i=0;i<M;i++) {
        cin >> a;
        int index = upper_bound(memo.begin(), memo.end(), -a) - memo.begin();
        if (index == N) {
            cout << -1 << endl;
        } else if (index == memo.size()) {
            cout << index+1 << endl;
            memo.push_back(-a);
        } else {
            cout << index+1 << endl;
            memo[index] = -a;
        }
    }
}
