#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N,K;
    cin >> N >> K;
    vector<vector<long long>> T(N, vector<long long>(N));
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            cin >> T[i][j];
        }
    }
    int ret = 0;
    vector<long long> v(N-1);
    iota(v.begin(), v.end(), 1);
    do {
        long long sum = 0;
        long long now = 0;
        for (int i=0;i<N-1;i++) {
            sum += T[now][v[i]];
            now = v[i];
        }
        sum += T[now][0];
        if (sum == K) {
            ret += 1;
        }
    } while (next_permutation(v.begin(), v.end()));
    cout << ret << endl;
}
