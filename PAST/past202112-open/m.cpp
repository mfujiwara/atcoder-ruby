#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<string> S;
    set<string> name_set;
    for (int i=0;i<N;i++) {
        string s;
        cin >> s;
        S.push_back(s);
        name_set.insert(s);
    }
    vector<pair<int,string>> queries;
    for (int i=0;i<Q;i++) {
        int x;
        string t;
        cin >> x >> t;
        queries.push_back(make_pair(x,t));
        name_set.insert(t);
    }
    map<string,int> name_map;
    map<int,string> name_map_inv;
    int index = 0;
    for (string name : name_set) {
        name_map[name] = index;
        name_map_inv[index] = name;
        index++;
    }
    tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update> st;
    for (int i=0;i<N;i++) {
        st.insert({name_map[S[i]], i});
    }
    for (int i=0;i<Q;i++) {
        int x = queries[i].first;
        string t = queries[i].second;
        auto itr = st.find_by_order(x-1);
        int k = itr->second;

        st.erase(itr);
        st.insert({name_map[t], k});
    }
    vector<string> rets = vector<string>(N);
    for (int i=0;i<N;i++) {
        auto itr = st.find_by_order(i);
        rets[itr->second] = name_map_inv[itr->first];
    }
    for (int i=0;i<N;i++) {
        cout << rets[i];
        if (i != N-1) {
            cout << " ";
        } else {
            cout << endl;
        }
    }
}
