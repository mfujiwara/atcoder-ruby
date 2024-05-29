#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int X,Y;
    cin >> X >> Y;
    if (Y==0) {
        cout << "ERROR" << endl;
    } else {
        int Z = X*100/Y;
        cout << Z/100 << "." << setw(2) << setfill('0') << Z%100 << endl;
    }
}
