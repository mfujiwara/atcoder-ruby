#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W;
    cin >> H >> W;
    vector<int> S(H);
    for (int i=0;i<H;i++) {
        string r;        
        cin >> r;
        S[i] = count(r.begin(), r.end(), '#');
    }
    vector<int> T(H);
    for (int i=0;i<H;i++) {
        string r;        
        cin >> r;
        T[i] = count(r.begin(), r.end(), '#');
    }
    if (S == T) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
