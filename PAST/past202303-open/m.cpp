#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

pair<long long,int> op(pair<long long,int> a, pair<long long,int> b) {
    if (a.second < b.second) return a;
    else return b;

}
pair<long long,int> e() { return {10000000000,1000000}; }

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> A;
    vector<pair<long long,int>> AwithIndex;
    vector<long long> B;
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        A.push_back(a);
        AwithIndex.push_back({a,i});
    }
    for (int i=0;i<M;i++) {
        long long b;
        cin >> b;
        B.push_back(b);
    }
    sort(AwithIndex.begin(),AwithIndex.end());
    map<int,int> indexMap;
    for (int i=0;i<N;i++) {
        indexMap[AwithIndex[i].second] = i;
    }
    segtree<pair<long long,int>,op,e> seg(AwithIndex);
    int bIndex = 0;    
    vector<long long> rets = vector<long long>(M,0);
    while (bIndex < M) {
        auto iter = lower_bound(AwithIndex.begin(), AwithIndex.end(), make_pair(B[bIndex],1000000));
        int position = distance(AwithIndex.begin(), iter);
        if (position == 0) {
            bIndex++;
            continue;
        }
        auto [minValue, index] = seg.prod(0, position);
        if (minValue > B[bIndex]) {
            bIndex++;
            continue;
        }
        seg.set(indexMap[index], {10000000000,1000000});
        B[bIndex] -= minValue;
        rets[bIndex] += minValue;
        A[index] = 0;
    }
    int b = N;
    for (int i=0;i<N;i++) {
        if (A[i] != 0) {
            b = i;
            break;
        }
    }
    if (b==N) {
        cout << "Yes" << endl;
        for (int i=0;i<M;i++) {
            cout << rets[i];
            if (i != M-1) cout << " ";
        }
        cout << endl;
    } else {
        cout << "No" << endl;
        cout << b+1 << endl;
    }
}
