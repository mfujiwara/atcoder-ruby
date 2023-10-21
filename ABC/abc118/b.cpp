#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> counts(M);
    for (int i=0;i<N;i++) {
        int K;
        cin >> K;
        for (int j=0;j<K;j++) {
            int A;
            cin >> A;
            counts[A-1]++;
        }
    }
    int ret=0;
    for (int i=0;i<M;i++) {
        if (counts[i]==N) {
            ret++;
        }
    }
    cout << ret << endl;
}
