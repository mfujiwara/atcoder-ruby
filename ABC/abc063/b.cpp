#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    set<char> st;
    for (int i = 0; i < S.size(); i++) {
        st.insert(S.at(i));
    }
    if (st.size() == S.size()) {
        cout << "yes" << endl;
    } else {
        cout << "no" << endl;
    }
}
