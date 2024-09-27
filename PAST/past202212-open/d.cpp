#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    string S;
    cin >> S;
    vector<int> hands(N);
    int field = 0;
    for (int i=0;i<S.size();i++) {
        int k = i%N;
        if (S[i]=='+') {
            hands[k] += field + 1;
            field = 0;
        } else if (S[i]=='-') {
            field += hands[k] + 1;
            hands[k] = 0;
        } else {
            hands[k] += 1;
        }
    }
    for (int i=0;i<N;i++) {
        cout << hands[i] << endl;
    }
}
