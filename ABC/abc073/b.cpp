#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret=0;
    for (int i=0;i<N;i++) {
        int l,r;
        cin >> l >> r;
        ret += r-l+1;
    }
    cout << ret << endl;
}
