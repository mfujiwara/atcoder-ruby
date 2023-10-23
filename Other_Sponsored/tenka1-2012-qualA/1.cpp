#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int m0=1;
    int m1=0;
    for (int i=0;i<n;i++) {
        int t0=m1;
        int t1=m0+m1;
        m0=t0;
        m1=t1;
    }
    cout << m0+m1 << endl;
}
