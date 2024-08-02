#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S;
    cin >> N >> S;
    vector<int> ret(N,-1);
    int first = -1;
    int tmp = -1;
    for (int i=0;i<N;i++) {
        if (S[i] == '1') {
            ret[i] = i+1;
        } else {
            ret[i] = tmp;
            tmp = i+1;
            if (first == -1) {
                first = i;
            }
        }
    }
    if (first != -1 && first+1 == tmp) {
        cout << -1 << endl;
    } else {
        if (first != -1) {
            ret[first] = tmp;
        }
        for (int i=0;i<N;i++) {
            cout << ret[i];
            if (i != N-1) {
                cout << " ";
            } else {
                cout << endl;
            }
        }
    }
}
