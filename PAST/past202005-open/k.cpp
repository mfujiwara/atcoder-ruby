#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<int> top(N);
    vector<int> below(N, -1);
    for (int i=0;i<N;i++) {
        top[i] = i;
    }
    for (int i=0;i<Q;i++) {
        int f,t,x;
        cin >> f >> t >> x;
        f--;t--;x--;
        int a = top[f];
        int b = top[t];
        int y = below[x];
        top[t] = a;
        below[x] = b;
        top[f] = y;
    }
    vector<int> rets(N);
    for (int i=0;i<N;i++) {
        int now = top[i];
        while (now != -1) {
            rets[now] = i+1;
            now = below[now];
        }
    }
    for (int i=0;i<N;i++) {
        cout << rets[i] << endl;
    }
}
