#include <bits/stdc++.h>
using namespace std;

int main() {
    string N;
    cin >> N;
    int n = 0;
    int s = 0;
    for (int i=0;i<N.size();i++) {
        n *= 10;
        n += N[i] - '0';
        s += N[i] - '0';
    }
    if (n % s == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
