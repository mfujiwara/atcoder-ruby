#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<string> S(5);
    for (int i=0;i<5;i++) {
        cin >> S[i];
    }

    for (int i=0;i<N;i++) {
        vector<string> T(5);
        for (int j=0;j<5;j++) {
            T[j] = S[j].substr(i*4,4);
        }
        if (T[1][2]=='#') {
            cout << 1;
        } else if (T[0][2]=='.') {
            cout << 4;
        } else if (T[2][1]=='.') {
            cout << 7;
        } else if (T[2][2]=='.') {
            cout << 0;
        } else {
            if (T[1][1]=='.') {
                if (T[3][1]=='#') {
                    cout << 2;
                } else {
                    cout << 3;
                }
            } else if (T[1][3]=='.') {
                if (T[3][1]=='.') {
                    cout << 5;
                } else {
                    cout << 6;
                }
            } else {
                if (T[3][1]=='#') {
                    cout << 8;
                } else {
                    cout << 9;
                }
            }
        }
    }
    cout << endl;
}
