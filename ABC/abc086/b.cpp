#include <bits/stdc++.h>
using namespace std;

int main() {
    string a,b;
    cin >> a >> b;
    int c = stoi(a+b);
    int d = sqrt(c);
    if (d*d == c) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
