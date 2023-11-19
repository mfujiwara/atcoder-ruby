#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> W(N);
    set<string> S;
    for (int i=0;i<N;i++) {
        cin >> W[i];
        S.insert(W[i]);
    }
    if (S.size() != N) {
        cout << "No" << endl;
        return 0;
    }
    for (int i=0;i<N-1;i++) {
        if (W[i].back() != W[i+1].front()) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}
