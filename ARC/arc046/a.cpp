#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int n = (N+8)/9;
    int d= N%9;
    if (d==0) d=9;
    for (int i=0;i<n;i++) {
        cout << d;
    }
    cout << endl;
}
