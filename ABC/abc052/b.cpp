#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;
    int x=0;
    int ret=0;
    for (int i=0;i<N;i++) {
        if (S[i]=='I') {
            x++;
        } else {
            x--;
        }
        ret=max(ret,x);
    }
    cout << ret << endl;
}
