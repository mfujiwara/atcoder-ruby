#include <bits/stdc++.h>
using namespace std;

int main() {
    string O,E;
    cin >> O >> E;
    string ret="";
    for (int i=0;i<O.size();i++) {
        ret+=O[i];
        if (i<E.size()) {
            ret+=E[i];
        }
    }
    cout << ret << endl;
}
