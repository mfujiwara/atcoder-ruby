#include <bits/stdc++.h>
using namespace std;

int main() {
    int X,N;
    cin >> X >> N;
    set<int> p;
    for (int i=0;i<N;i++) {
        int tmp;
        cin >> tmp;
        p.insert(tmp);
    }
    int diff = 0;
    while (true) {
        if (p.find(X-diff) == p.end()) {
            cout << X-diff << endl;
            return 0;
        }
        if (p.find(X+diff) == p.end()) {
            cout << X+diff << endl;
            return 0;
        }
        diff++;
    }
}
