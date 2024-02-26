#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int c = 0;
    for (int i=0;i<S.size();i++) {
        if (c==0 && (S[i]=='I' || S[i]=='i')) {
            c++;
        } else if (c==1 && (S[i]=='C' || S[i]=='c')) {
            c++;
        } else if (c==2 && (S[i]=='T' || S[i]=='t')) {
            c++;
        }
    }
    if (c==3) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
