#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ret = 1000;
    for (int i=0;i<S.size()-2;i++) {
        int tmp = stoi(S.substr(i,3));
        ret = min(ret, abs(tmp-753));
    }
    cout << ret << endl;
}
