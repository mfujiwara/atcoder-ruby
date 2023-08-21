#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret=0;
    for (int i=0;i<N;i++) {
        int m;
        cin >> m;
        ret += max(80-m,0);
    }
    cout << ret << endl;
}
