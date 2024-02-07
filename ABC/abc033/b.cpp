#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    int P;
    vector<pair<string, int>> vec(N);
    int total = 0;
    for (int i=0;i<N;i++) {
        cin >> S >> P;
        vec[i] = make_pair(S, P);
        total += P;
    }
    for (int i=0;i<N;i++) {
        if (vec[i].second*2 > total) {
            cout << vec[i].first << endl;
            return 0;
        }
    }
    cout << "atcoder" << endl;
}
