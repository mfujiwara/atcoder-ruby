#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long N,M;
    cin >> N >> M;
    // 長さMの文字の文字列
    string S = "";
    long long t = 1;
    for (int i=0;i<M;i++) {
        if (t>1000000000) {
            S += "x";
            continue;
        }
        t *= N;
        if (t>1000000000) {
            S += "x";
        } else {
            S += "o";
        }
    }
    cout << S << endl;
}
