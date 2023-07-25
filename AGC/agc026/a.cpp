#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int a;
    int pre=-1;
    int ret=0;
    for (int i=0;i<N;i++) {
        cin >> a;
        if (a==pre) {
            ret++;
            pre=-1;
        } else {
            pre=a;
        }
    }
    cout << ret << endl;
}
