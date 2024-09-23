#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<long long> P(N);
    vector<long long> sss;
    for (int i=0;i<N;i++) {
        cin >> P[i];
        sss.push_back(P[i]);
    }
    vector<vector<long long>> queries(Q, vector<long long>(3));
    for (int i=0;i<Q;i++) {
        int t;
        cin >> t;
        queries[i][0] = t;
        if (t == 1) {
            cin >> queries[i][1] >> queries[i][2];
            sss.push_back(queries[i][2]);
        } else {
            cin >> queries[i][1];
        }
        queries[i][1]--;
    }
    sort(sss.begin(), sss.end());
    map<long long,int> mp;
    for (int i=0;i<sss.size();i++) {
        mp[sss[i]] = i;
    }
    tree<pair<int,int>, null_type, greater<pair<int,int>>, rb_tree_tag, tree_order_statistics_node_update> st;
    for (int i=0;i<N;i++) {
        P[i] = mp[P[i]];
        st.insert({P[i], i});
    }
    for (int i=0;i<Q;i++) {
        if (queries[i][0] == 1) {
            queries[i][2] = mp[queries[i][2]];
        }
    }
    for (int i=0;i<Q;i++) {
        if (queries[i][0] == 1) {
            int idx = queries[i][1];
            int val = queries[i][2];
            st.erase({P[idx], idx});
            P[idx] = val;
            st.insert({P[idx], idx});
       } else if (queries[i][0] == 2) {
            int idx = queries[i][1];
            auto order = st.order_of_key({P[idx], idx});
            cout << order+1 << endl;
        } else {
            int order = queries[i][1];
            auto iter = st.find_by_order(order);
            cout << iter->second+1 << endl;
        }
    }
}
