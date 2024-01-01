#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    if (S[0]!='A') {
        cout << "WA" << endl;
        return 0;
    }
    int count = 0;
    int cindex = 0;
    for (int i=2;i<S.size()-1;i++) {
        if (S[i]=='C') {
            count++;
            cindex = i;
        }
    }
    if (count!=1) {
        cout << "WA" << endl;
        return 0;
    }
    for (int i=1;i<S.size();i++) {
        if (i==cindex) {
            continue;
        }
        if (S[i]<'a' || S[i]>'z') {
            cout << "WA" << endl;
            return 0;
        }
    }
    cout << "AC" << endl;
}
