#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    int M = (N-2)/2;
    int total = 0;
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        total += a;
    }
    map<pair<int,int>,double> dp = {{{0,total},0}};
    for (int i=0;i<N-2;i++) {
        map<pair<int,int>,double> next;
        for (auto p:dp) {
            int now = p.first.first;
            int rest = p.first.second;
            double v = p.second;
            if (i<=M) {
                if (rest-now < 0) {
                    continue;
                }
                for (int j=now;j<=rest;j++) {
                    auto key1 = make_pair(j,rest-j);
                    double v1 = v+sqrt(1+(now-j)*(now-j));
                    if (next.find(key1) == next.end()) {
                        next[key1] = v1;
                    } else {
                        next[key1] = min(next[key1],v1);
                    }
                }
            } else {
                for (int j=0;j<=min(now,rest);j++) {
                    auto key1 = make_pair(j,rest-j);
                    double v1 = v+sqrt(1+(now-j)*(now-j));
                    if (next.find(key1) == next.end()) {
                        next[key1] = v1;
                    } else {
                        next[key1] = min(next[key1],v1);
                    }
                }
            }
        }
        dp = next;
    }
    double ret = 1e9;
    for (auto p:dp) {
        int now = p.first.first;
        int rest = p.first.second;
        double v = p.second;
        if (rest == 0) {
            ret = min(ret,v+sqrt(1+now*now));
        }
    }
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
