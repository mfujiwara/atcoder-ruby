#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> d(7);
    for (int i=0;i<7;i++) {
        cin >> d[i];
    }
    vector<int> j(7);
    for (int i=0;i<7;i++) {
        cin >> j[i];
    }
    int ret=0;
    for (int i=0;i<7;i++) {
        ret += max(d[i], j[i]);
    }
    cout << ret << endl;
}
