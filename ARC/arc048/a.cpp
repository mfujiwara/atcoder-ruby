#include <bits/stdc++.h>
using namespace std;

int main() {
    long A,B;
    cin >> A >> B;
    if (A*B>0) {
        cout << B-A << endl;
    } else {
        cout << B-A-1 << endl;
    }
}
