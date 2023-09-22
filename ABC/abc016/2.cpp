#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    if (C==A+B && C==A-B) {
        cout << "?" << endl;
    } else if (C==A+B) {
        cout << "+" << endl;
    } else if (C==A-B) {
        cout << "-" << endl;
    } else {
        cout << "!" << endl;
    }
}
