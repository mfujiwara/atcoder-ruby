#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    set<int> s;
    for (int k=0; k<K; k++) {
        int d;
        cin >> d;
        for (int i=0; i<d; i++) {
            int a;
            cin >> a;
            s.insert(a);
        }
    }
    cout << N-s.size() << endl;
}
