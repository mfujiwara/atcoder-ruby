#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S;
    cin >> N >> S;
    vector<int> perm(N);
    iota(perm.begin(), perm.end(), 0);
    do {
        string T = S;
        for (int i = 0; i < N; i++) {
            T[i] = S[perm[i]];
        }
        if (T!=S && T!=string(S.rbegin(), S.rend())) {
            cout << T << endl;
            return 0;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    cout << "None" << endl;    
}
