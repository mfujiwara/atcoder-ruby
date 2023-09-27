#include <bits/stdc++.h>
using namespace std;

int main() {
    int X;
    cin >> X;
    for (int i=0;i<1000;i++) {
        if (i*i*i*i == X) {
            cout << i << endl;
            return 0;
        }
    }
}
