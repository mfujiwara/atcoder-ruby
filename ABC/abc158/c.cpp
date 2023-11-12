#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B;
    cin >> A >> B;
    int ret=-1;
    for (int i=0;i<10000;i++) {
        if (i*8/100==A && i/10==B) {
            ret=i;
            break;
        }
    }
    cout << ret << endl;
}
