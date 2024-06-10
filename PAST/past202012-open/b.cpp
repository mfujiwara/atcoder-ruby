#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S;
    cin >> N >> S;
    set<char> st;
    string T = "";
    for (int i=S.size()-1;i>=0;i--) {
        if (st.find(S[i]) == st.end()) {
            st.insert(S[i]);
            T = S[i] + T;
        }
    }
    cout << T << endl;
}
