#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    map<long long, int> cnt;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        cnt[A[i]]++;
    }
    sort(A.begin(), A.end());
    int ret = N;
    for (int i=2;i<N;i++) {
        if (cnt[A[i]]>0 && cnt[A[i]-1]>0 && cnt[A[i]-2]>0) {
            cnt[A[i]]--;
            cnt[A[i]-1]--;
            cnt[A[i]-2]--;
            ret-=3;
        }
    }
    cout << ret << endl;
}
