#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,L;
    cin >> N >> L;
    string S;
    cin >> S;
    int ret=0;
    int now=1;
    for (int i=0;i<N;i++) {
        if (S[i]=='+') {
            now++;
            if (now>L) {
                ret++;
                now=1;
            }
        } else {
            now--;
        }
    }
    cout << ret << endl;
}
