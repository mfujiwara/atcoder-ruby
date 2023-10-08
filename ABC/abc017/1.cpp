#include <bits/stdc++.h>
using namespace std;

int main() {
    int ret=0;
    for (int i=0;i<3;i++) {
        int s,e;
        cin >> s >> e;
        ret += s*e/10;
    }
    cout << ret << endl;
}
