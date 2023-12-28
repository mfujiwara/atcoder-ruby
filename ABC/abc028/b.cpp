#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    vector<int> count(6,0);
    for (int i=0;i<S.size();i++) {
        count[S[i]-'A']++;
    }
    for (int i=0;i<6;i++) {
        cout << count[i];
        if (i!=5) {
            cout << " ";
        } else {
            cout << endl;
        }
    }
}
