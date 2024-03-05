#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<pair<long long, long long>> AB(N);
    long long A,B;
    for (int i=0;i<N;i++) {
        cin >> A >> B;
        AB[i] = make_pair(A,B);
    }
    sort(AB.begin(), AB.end());
    long long ret = 0;
    for (int i=0;i<N;i++) {
        if (M > AB[i].second) {
            ret += AB[i].first * AB[i].second;
            M -= AB[i].second;
        } else {
            ret += AB[i].first * M;
            break;
        }
    }
    cout << ret << endl;
}
