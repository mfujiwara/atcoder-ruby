#include <bits/stdc++.h>
using namespace std;

int main() {
    string name;
    cin >> name;
    for (int i=0;i<name.size()/2;i++) {
        if (name[i] != name[name.size()-1-i]) {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}
