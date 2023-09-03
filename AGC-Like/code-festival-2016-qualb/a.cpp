#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ret=0;
    string T="CODEFESTIVAL2016";
    for (int i=0;i<S.size();i++) {
        if (S[i]!=T[i]) {
            ret++;
        }
    }
    cout << ret << endl;
}
