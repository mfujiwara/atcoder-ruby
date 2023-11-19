#include <bits/stdc++.h>
using namespace std;

int main() {
    int tmp;
    int ret=0;
    for (int i=0;i<3;i++) {
        cin >> tmp;
        ret ^= tmp;
    }
    cout << ret << endl;
}
