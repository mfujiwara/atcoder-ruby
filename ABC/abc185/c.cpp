#include <bits/stdc++.h>
using namespace std;

int main() {
    int L;
    cin >> L;
    long long ret = 1;
    for (int i=1;i<=11;i++) {
        ret *= L-i;
        ret /= i;
    }
    cout << ret << endl;
}
