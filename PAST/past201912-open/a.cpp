#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ret = 0;
    for (int i=0;i<S.size();i++) {
        ret*=10;
        if ('0' <= S[i] && S[i] <= '9') {
           ret+=S[i]-'0';
        } else {
            cout << "error" << endl;
            return 0;
        }
    }
    cout << ret*2 << endl;
}
