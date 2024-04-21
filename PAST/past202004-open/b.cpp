#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    int a=0,b=0,c=0;
    for (int i=0;i<S.size();i++) {
        if (S[i] == 'a') {
            a+=1;
        } else if (S[i] == 'b') {
            b+=1;
        } else {
            c+=1;
        }
    }
    if (a>b && a>c) {
        cout << "a" << endl;
    } else if (b>a && b>c) {
        cout << "b" << endl;
    } else {
        cout << "c" << endl;
    }
}
