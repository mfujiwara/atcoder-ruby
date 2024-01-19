#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    int A,B,C,D;
    cin >> S >> A >> B >> C >> D;
    for (int i=0;i<S.size();i++) {
        if (i==A || i==B || i==C || i==D) {
            cout << "\"";
        }
        cout << S[i];
    }
    if (S.size()==D) {
        cout << "\"";
    }
    cout << endl;
}
