#include <bits/stdc++.h>
using namespace std;

int main() {
    string w;
    cin >> w;
    vector<int> counts(26, 0);
    for (int i=0;i<w.size();i++) {
        counts[w[i]-'a']++;
    }
    for (int i=0;i<26;i++) {
        if (counts[i]%2==1) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}
