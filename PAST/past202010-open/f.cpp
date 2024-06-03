#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,K;
    cin >> N >> K;
    map<string,int> counts;
    string s;
    for (int i=0;i<N;i++) {
        cin >> s;
        counts[s]++;
    }
    vector<pair<int,string>> v;
    v.push_back({0,""});
    v.push_back({N+1,""});
    for (auto p:counts) {
        v.push_back({p.second,p.first});
    }
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());
    string ret = v[K].second;
    if (v[K].first == v[K+1].first || v[K].first == v[K-1].first) {
        cout << "AMBIGUOUS" << endl;
    } else {
        cout << ret << endl;
    }
}
