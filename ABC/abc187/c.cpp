#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    set<string> S0;
    set<string> S1;
    for (int i=0;i<N;i++) {
        string S;
        cin >> S;
        if (S[0] == '!') {
            S1.insert(S.substr(1));
        } else {
            S0.insert(S);
        }
    }
    for (auto s : S0) {
        if (S1.find(s) != S1.end()) {
            cout << s << endl;
            return 0;
        }
    }
    cout << "satisfiable" << endl;
}
