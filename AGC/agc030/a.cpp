#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    if (B>=C) {
        cout << B+C << endl;
    } else if (A+B>=C) {
        cout << B+C << endl;
    } else {
        cout << 2*B+A+1 << endl;
    }
}
