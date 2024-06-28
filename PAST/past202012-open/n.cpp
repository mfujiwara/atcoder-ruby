#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<long long> lefts(N);
    vector<long long> rights(N);
    for (int i=0;i<N-1;i++) {
        cin >> lefts[i] >> rights[i];
    }
    vector<set<int>> start(N);
    vector<long long> ages(Q);
    for (int i=0;i<Q;i++) {
        int b;
        cin >> ages[i] >> b;
        b--;
        start[b].insert(i);
    }

    set<int> now;
    priority_queue<pair<long long,int>> pq0;
    priority_queue<pair<long long,int>> pq1;

    vector<int> right(Q);
    now = start[0];
    pq0 = priority_queue<pair<long long,int>>();
    pq1 = priority_queue<pair<long long,int>>();
    for (auto x:now) {
        pq0.push({-ages[x],x});
        pq1.push({ages[x],x});
    }
    for (int i=0;i<N-1;i++) {
        while (pq0.size() > 0){
            auto [age,x] = pq0.top();
            age = -age;
            if (now.count(x) == 0) {
                pq0.pop();
                continue;
            } else if (age < lefts[i]) {
                pq0.pop();
                now.erase(x);
                right[x] = i;
            } else {
                break;
            }
        }
        while (pq1.size() > 0) {
            auto [age,x] = pq1.top();
            if (now.count(x) == 0) {
                pq1.pop();
                continue;
            } else if (age > rights[i]) {
                pq1.pop();
                now.erase(x);
                right[x] = i;
            } else {
                break;
            }
        }
        for (int x:start[i+1]) {
            now.insert(x);
            pq0.push({-ages[x],x});
            pq1.push({ages[x],x});
        }
    }
    for (int x:now) {
        right[x] = N-1;
    }

    vector<int> left(Q);
    now = start[N-1];
    pq0 = priority_queue<pair<long long,int>>();
    pq1 = priority_queue<pair<long long,int>>();
    for (auto x:now) {
        pq0.push({-ages[x],x});
        pq1.push({ages[x],x});
    }
    for (int i=N-1;i>0;i--) {
        while (pq0.size() > 0){
            auto [age,x] = pq0.top();
            age = -age;
            if (now.count(x) == 0) {
                pq0.pop();
                continue;
            } else if (age < lefts[i-1]) {
                pq0.pop();
                now.erase(x);
                left[x] = i;
            } else {
                break;
            }
        }
        while (pq1.size() > 0) {
            auto [age,x] = pq1.top();
            if (now.count(x) == 0) {
                pq1.pop();
                continue;
            } else if (age > rights[i-1]) {
                pq1.pop();
                now.erase(x);
                left[x] = i;
            } else {
                break;
            }
        }
        for (int x:start[i-1]) {
            now.insert(x);
            pq0.push({-ages[x],x});
            pq1.push({ages[x],x});
        }
    }
    for (int x:now) {
        left[x] = 0;
    }
    for (int i=0;i<Q;i++) {
        cout << right[i]-left[i]+1 << endl;
    }
}
