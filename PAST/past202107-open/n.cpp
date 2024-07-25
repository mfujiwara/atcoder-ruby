#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

pair<long long,long long> op(pair<long long,long long> l, pair<long long,long long> r) { 
    return make_pair(l.first+r.first,l.second+r.second); 
}
pair<long long,long long> e() { return make_pair(0,0); }
pair<long long,long long> mapping(int lazyL, pair<long long,long long> r) {
    if (lazyL%2==0) {
        return r;
    } else {
        return make_pair(r.second,r.first);
    }
}
int composition(int lazyL, int lazyR) { return (lazyL+lazyR)%2; }
int id() { return 0; }

int main() {
    int Q;
    cin >> Q;    
    set<long long> x_set;
    vector<tuple<long long,long long,long long>> yxx;
    for (int i=0;i<Q;i++) {
        long long a,b,c,d;
        cin >> a >> b >> c >> d;
        x_set.insert(a);
        x_set.insert(c);
        yxx.push_back(make_tuple(b,a,c));
        yxx.push_back(make_tuple(d,a,c));
    }
    sort(yxx.begin(),yxx.end());
    vector<long long> x;
    for (auto xx:x_set) {
        x.push_back(xx);
    }
    sort(x.begin(),x.end());
    map<long long,int> x_map;
    for (int i=0;i<int(x.size());i++) {
        x_map[x[i]] = i;
    }
    vector<pair<long long,long long>> arr;
    for (int i=0;i<int(x.size()-1);i++) {
        arr.push_back(make_pair(0,x[i+1]-x[i]));
    }
    lazy_segtree<pair<long long,long long>,op,e,int,mapping,composition,id> seg(arr);
    long long pre_y = 0;
    long long ret = 0;
    for (int i=0;i<int(yxx.size());i++) {
        long long y,a,c;
        tie(y,a,c) = yxx[i];
        ret += seg.all_prod().first*(y-pre_y);
        seg.apply(x_map[a],x_map[c],1);
        pre_y = y;
    }
    cout << ret << endl;
}
