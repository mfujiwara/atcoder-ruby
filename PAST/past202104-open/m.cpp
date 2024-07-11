#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    map<long long,long long> counts;
    long long ret = 0;
    map<int, pair<long long,int>> ends;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        ret += counts[A[i]];
        counts[A[i]]++;
        if (i==0) {
            ends[i] = {A[i],i};
        } else if(A[i]==A[i-1]) {
            auto [a,b] = ends[i-1];
            ends.erase(i-1);
            ends[i] = {A[i],b};
        } else {
            ends[i] = {A[i],i};
        }
    }
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int l,r;
        long long x;
        cin >> l >> r >> x;
        l--;
        r--;
        vector<int> keys;
        auto iter = ends.lower_bound(l);
        while (iter!=ends.end() && iter->second.second<=r) {
            keys.push_back(iter->first);
            iter++;
        }
        map<long long,int> diffs;
        for (int t:keys) {
            auto [v,s] = ends[t];
            if (s<l && r<t) {
                diffs[v] -= r-l+1;
                ends[t] = {v,r+1};
                ends[l-1] = {v,s};
            } else if (s<l) {
                diffs[v] -= t-l+1;
                ends.erase(t);
                ends[l-1] = {v,s};
            } else if (r<t) {
                diffs[v] -= r-s+1;
                ends[t] = {v,r+1};
            } else {
                diffs[v] -= t-s+1;
                ends.erase(t);
            }
        }
        diffs[x] += r-l+1;
        ends[r] = {x,l};
        for (auto [a,b]:diffs) {
            ret -= counts[a]*(counts[a]-1)/2;
            counts[a] += b;
            ret += counts[a]*(counts[a]-1)/2;
        }
        cout << ret << endl;
    }
}
