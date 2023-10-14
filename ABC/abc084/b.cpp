#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B;
    string S;
    cin >> A >> B >> S;
    for (int i=0;i<A+B+1;i++) {
        if (i==A) {
            if (S[i]!='-') {
                cout << "No" << endl;
                return 0;
            }
        } else {
            if (S[i]<'0' || S[i]>'9') {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
}
