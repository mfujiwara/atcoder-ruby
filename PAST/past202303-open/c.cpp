#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    map<int, int> mp;
    for (int i=0;i<N;i++) {
        int p;
        cin >> p;
        mp[p]=i+1;
    }
    for (int i=1;i<=N;i++) {
        cout << mp[i];
        if (i!=N) cout << " ";
    }
    cout << endl;
}
