#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int a = stoi(S.substr(0, 2));
    int b = stoi(S.substr(2, 2));
    if (0<a && a<=12) {
        if (0<b && b<=12) {
            cout << "AMBIGUOUS" << endl;
        } else {
            cout << "MMYY" << endl;
        }
    } else {
        if (0<b && b<=12) {
            cout << "YYMM" << endl;
        } else {
            cout << "NA" << endl;
        }
    }
}
