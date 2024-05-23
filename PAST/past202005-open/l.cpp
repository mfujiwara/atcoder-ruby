#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<int> top(N, 1);
    vector<vector<long long>> T(N, vector<long long>());
    map<long long, int> index;
    for (int i=0;i<N;i++) {
        int K;
        cin >> K;
        for (int j=0;j<K;j++) {
            long long t;
            cin >> t;
            T[i].push_back(t);
            index[t] = i;
        }
        T[i].push_back(0);
        T[i].push_back(0);
    }
    priority_queue<long long> pq1;
    set<long long> set1;
    priority_queue<long long> pq2;
    for (int i=0;i<N;i++) {
        pq1.push(T[i][0]);
        pq2.push(T[i][0]);
        set1.insert(T[i][0]);
        if (T[i].size() > 1) {
            pq2.push(T[i][1]);
        }
    }
    set<long long> done;
    int M;
    cin >> M;
    for (int i=0;i<M;i++) {
        int a;
        cin >> a;
        if (a==1) {
            long long x = pq1.top();
            pq1.pop();
            done.insert(x);
            set1.erase(x);
            cout << x << endl;
            int i = index[x];
            pq1.push(T[i][top[i]]);
            set1.insert(T[i][top[i]]);
            pq2.push(T[i][top[i]+1]);
            top[i]++;
        } else {
            long long x = pq2.top();
            pq2.pop();
            while (done.find(x) != done.end()) {
                x = pq2.top();
                pq2.pop();
            }
            done.insert(x);
            cout << x << endl;
            int i = index[x];
            if (set1.find(x) != set1.end()) {
                pq1.pop();
                set1.erase(x);
                pq1.push(T[i][top[i]]);
                set1.insert(T[i][top[i]]);
                pq2.push(T[i][top[i]+1]);
                top[i]++;
            } else {
                pq2.push(T[i][top[i]+1]);
                top[i]++;
            }
        }
    }
}
