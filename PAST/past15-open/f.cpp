#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<pair<int,int>> A;
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        A.push_back({a,i});
    }
    sort(A.begin(),A.end());
    vector<int> B(N);
    for (int i=0;i<N;i++) {
        B[A[i].second] = i+1;
    }
    for (int i=0;i<N;i++) {
        cout << B[i];
        if (i<N-1) cout << " ";
    }
    cout << endl;
}
