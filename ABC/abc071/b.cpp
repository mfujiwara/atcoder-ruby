#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    set<char> st;
    for (int i=0;i<S.size();i++) {
        st.insert(S[i]);
    }
    for (char c='a';c<='z';c++) {
        if (st.find(c) == st.end()) {
            cout << c << endl;
            return 0;
        }
    }
    cout << "None" << endl;
}
