#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N,x;
    cin >> N >> x;
    vector<long long> a(N);
    for (int i=0;i<N;i++) {
        cin>>a[i];
    }
    sort(a.begin(), a.end());
    long long ret = 0;
    for (int i=0;i<N;i++) {
        if (x >= a[i]) {
            ret++;
            x -= a[i];
        } else {
            break;
        }
    }
    if (ret == N && x > 0) {
        ret--;
    }
    cout << ret << endl;
}
