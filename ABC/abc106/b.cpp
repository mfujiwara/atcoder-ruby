#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret=0;
    for (int i=105;i<=N;i+=2) {
        int cnt=0;
        for (int j=1;j<=i;j++) {
            if (i%j==0) {
                cnt++;
            }
        }
        if (cnt==8) {
            ret++;
        }
    }
    cout << ret << endl;
}
