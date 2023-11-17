#include <bits/stdc++.h>
using namespace std;

int main() {
    int X;
    cin >> X;
    vector<bool> memo(100003, true);
    memo[0]=false;
    memo[1]=false;
    for (int i=2;i<100004;i++) {
        if (memo[i]==false) continue;
        if (i>=X) {
            cout << i << endl;
            return 0;
        }
        for (int j=2;i*j<=100004;j++) {
            memo[i*j]=false;
        }
    }
}
