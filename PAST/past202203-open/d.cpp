#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int T,N;
    cin >> T >> N;
    vector<int> maxi = vector<int>(N,0);
    int t;
    for (int i=0;i<T;i++) {
        for (int j=0;j<N;j++) {
            cin >> t;
            maxi[j] = max(maxi[j],t);
        }
        cout << reduce(maxi.begin(),maxi.end()) << endl;
    }
}
