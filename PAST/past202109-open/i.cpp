#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    priority_queue<long long> pq;
    int c=0;
    for (int i=0;i<N;i++) {
        long long A;
        cin >> A;
        while (A%2==0) {
            A/=2;
            c++;
        }
        pq.push(-A);
    }
    while (c>0) {
        auto v = pq.top();
        pq.pop();
        v *= 3;
        pq.push(v);
        c--;
    }
    cout << -pq.top() << endl;
}
