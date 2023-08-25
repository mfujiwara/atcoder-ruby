#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ret=0;
    int now=0;
    for (int i=0;i<S.size();i++) {
        if (S[i]=='A' || S[i]=='C' || S[i]=='G' || S[i]=='T') {
            now++;
            ret=max(ret,now);
        } else {
            now=0;
        }
    }
    cout << ret << endl;
}
