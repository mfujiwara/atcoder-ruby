#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    if (A>B) {
        if (B>C) {
            cout << 1 << endl;
            cout << 2 << endl;
            cout << 3 << endl;
        } else {
            if (A>C) {
                cout << 1 << endl;
                cout << 3 << endl;
                cout << 2 << endl;
            } else {
                cout << 2 << endl;
                cout << 3 << endl;
                cout << 1 << endl;
            }
        }
    } else {
        if (A>C) {
            cout << 2 << endl;
            cout << 1 << endl;
            cout << 3 << endl;
        } else {
            if (B>C) {
                cout << 3 << endl;
                cout << 1 << endl;
                cout << 2 << endl;
            } else {
                cout << 3 << endl;
                cout << 2 << endl;
                cout << 1 << endl;
            }
        }
    }
}
