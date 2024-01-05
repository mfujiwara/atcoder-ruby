#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> memo(N, 0);
    int L,R;
    for (int i=0;i<M;i++) {        
        cin >> L >> R;
        memo[L-1]++;
        memo[R]--;
    }
    int sum = 0;
    int ret = 0;
    for (int i=0;i<N;i++) {
        sum += memo[i];
        if (sum == M) {
            ret++;
        }
    }
    cout << ret << endl;
}
