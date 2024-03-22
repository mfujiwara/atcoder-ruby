#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,a,b,K;
    cin >> N >> a >> b >> K;
    set<int> s;
    s.insert(a);
    s.insert(b);
    for (int i=0;i<K;i++) {
        int P;
        cin >> P;
        s.insert(P);
    }
    if (s.size() == K+2) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
