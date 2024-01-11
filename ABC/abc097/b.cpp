#include <bits/stdc++.h>
using namespace std;

int main() {
    int X;
    cin >> X;
    int ret=1;
    for (int b=2;b<=X;b++) {
        int p=b*b;
        while (p<=X) {
            ret=max(ret,p);
            p*=b;
        }
    }
    cout << ret << endl;
}
