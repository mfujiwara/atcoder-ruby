#include <bits/stdc++.h>
using namespace std;

int main() {
    string W;
    cin >> W;
    for (int i=0;i<W.size();i++) {
        if (W[i]!='a' && W[i]!='e' && W[i]!='i' && W[i]!='o' && W[i]!='u') {
            cout << W[i];
        }
    }
    cout << endl;
}
