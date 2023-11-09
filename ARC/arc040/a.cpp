#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int r=0,b=0;
    for (int i=0;i<N;i++) {
        string s;
        cin >> s;
        for (int j=0;j<N;j++) {
            if (s[j]=='R') {
                r++;
            } else if (s[j]=='B') {
                b++;
            }
        }
    }
    if (r>b) {
        cout << "TAKAHASHI" << endl;
    } else if (r<b) {
        cout << "AOKI" << endl;
    } else {
        cout << "DRAW" << endl;
    }
}
